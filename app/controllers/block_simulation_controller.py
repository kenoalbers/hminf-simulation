import numpy as np

from matplotlib.animation import FuncAnimation

from app.models import BlockSimulationModel, ForceModel
from app.views import BlockSimulationView


class BlockSimulationController:
    def __init__(self, model: BlockSimulationModel, view: BlockSimulationView):
        self.model = model
        self.view = view
        self.animation = None
        self.forces = ForceModel()

    def run(self):
        self.view.initialize_view(self.model)

        # Connect widgets to methods
        self.view.angle_slider.on_changed(self._update_angle)
        self.view.width_slider.on_changed(self._update_width)
        self.view.coefficient_still_slider.on_changed(self._update_coefficient_still)
        self.view.coefficient_moving_slider.on_changed(self._update_coefficient_moving)

        # Start animation on button clicked
        self.view.start_button.on_clicked(self.start_animation)

        self.view.show()

    def start_animation(self, event):
        # Start matplotlib FuncAnimation
        self.animation = FuncAnimation(
            fig=self.view.figure,
            func=self.update_animation,
            init_func=self.initialize_animation,
            frames=1000,
            interval=33.33,
            repeat=False
        )

        # Update
        self.view.figure.canvas.draw_idle()

    def initialize_animation(self):
        # Deactivate sliders
        self.view.angle_slider.set_active(False)
        self.view.width_slider.set_active(False)
        self.view.coefficient_still_slider.set_active(False)
        self.view.coefficient_moving_slider.set_active(False)

        # Remove button
        self.view.start_button.ax.set_visible(False)
        self.view.start_button.set_active(False)

        # Place sliding block
        self.model.block1_position = (0, self.model.get_opposite_length(2))
        self.view.sliding_block_patch.set_xy(self.model.block1_position)

        # Mass
        mass = self.model.width / 3

        # Calculate simulated G and grade forces (width is equal to weight for simulation purposes)
        self.forces.g_force = mass * 9.81
        print(f'G force: {self.forces.g_force}')

        self.forces.grade_force = self.forces.g_force * np.sin(np.radians(self.model.angle))
        print(f'Grade force: {self.forces.grade_force}')

        self.forces.friction_force_still = self.model.coefficient_still * self.forces.g_force * np.cos(
            np.radians(self.model.angle))
        print(f'Friction force still: {self.forces.friction_force_still}')

        if self.forces.grade_force > self.forces.friction_force_still:
            self.forces.friction_force_moving = self.model.coefficient_moving * self.forces.g_force * np.cos(
                np.radians(self.model.angle))
            print(f'Friction force moving: {self.forces.friction_force_moving}')

            # Calculate resulting acceleration
            resulting_force = self.forces.grade_force - self.forces.friction_force_moving

            self.forces.acceleration = resulting_force / mass

            if resulting_force < 0:
                self.forces.acceleration = 0
                print("Block won't move because of friction forces when moving.")

            print(f'Acceleration: {self.forces.acceleration}')

        else:
            print("Block won't move because of friction forces when standing still.")

        return self.view.angle_slider

    def update_animation(self, frame):
        frame_time = frame / 50

        # Calculate progress with acceleration
        progress = 0.5 * self.forces.acceleration * frame_time ** 2

        self.model.block1_position = (progress, self.model.get_opposite_length(2 - progress))

        # Check if a hit occurred
        if (self.model.block1_position[1] - (self.model.width * np.sin(np.radians(self.model.angle)))) > 0:
            self.view.sliding_block_patch.set_xy(self.model.block1_position)
        else:

            if not self.forces.collision:
                # Remember frame
                self.forces.collision_frame = frame

                # Calculate impuls
                # p = m * v (v in direction of travel)
                self.forces.impuls = (self.model.width / 3) * (
                        (self.forces.acceleration * frame_time) * np.cos(np.radians(self.model.angle)))
                print(f'HIT -> Frame: {self.forces.collision_frame} Force: {self.forces.impuls}')

                # Calculate start speed of collision block
                # v_o = p / m
                self.forces.block2_velocity = (self.forces.impuls / (0.3 / 3)) / 10
                print(f'Initial speed block: {self.forces.block2_velocity}')

                # Stopping forces
                self.forces.block2_acceleration = -self.model.coefficient_moving * 9.81
                print(f'Stopping motion {self.model.coefficient_moving}: {self.forces.block2_acceleration}')
            else:
                frame_delta = (frame - self.forces.collision_frame) / 50
                next_frame_delta = ((frame+1) - self.forces.collision_frame) / 50

                progress_collision = (self.model.block2_position[0] + self.forces.block2_velocity * frame_delta + 0.5 * self.forces.block2_acceleration * frame_delta ** 2)
                next_collision = (self.model.block2_position[0] + self.forces.block2_velocity * next_frame_delta + 0.5 * self.forces.block2_acceleration * next_frame_delta ** 2)

                if next_collision > progress_collision:
                    self.model.block2_position = (progress_collision, 0)
                    self.view.collision_block_patch.set_xy(self.model.block2_position)
                else:
                    print(self.model.block2_position[0])

            self.forces.collision = True

        return self.view.sliding_block_patch

    # Update widgets functionality
    def _update_angle(self, value):
        self.model.angle = value
        self.view.update_view(self.model)

    def _update_width(self, value):
        self.model.width = value
        self.view.update_view(self.model)

    def _update_coefficient_still(self, value):
        self.model.coefficient_still = value
        self.view.update_view(self.model)

    def _update_coefficient_moving(self, value):
        self.model.coefficient_moving = value
        self.view.update_view(self.model)
