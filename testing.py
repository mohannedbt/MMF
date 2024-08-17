from manim import *
import numpy as np
from math import*

class Join(Scene):
    def construct(self):
        lim=Tex(r"\[\lim_{a \to b} \frac{f(b)-f(a)}{b-a}\]",font_size=50)
        lim_title=Tex(r"the derivative formula")
        lim.shift(2*UP)
        lim_title.shift(1*DOWN)
        rect=Rectangle(color=BLUE).surround(lim)
        self.play(Write(lim),run_time=3)
        self.wait(5)
        self.play(Write(lim_title),Create(rect),run_time=2)
        self.wait(3)
        self.remove(lim,lim_title,rect)
        # Create axes
        ax = Axes(
            x_range=[-2, 7, 1],
            y_range=[0, 5, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )
        
        # Create labels for points A and B
        label_a = Text("A", font_size=35)
        label_b = Text("B", font_size=35)
        label_f=Tex(r"\[f(x)=e^x\]")
        label_f.shift([3,2.5,0])
        remarque=Tex(r"\[B(\frac{1}{2},e^{\frac{1}{2}})\]")
        remarque.set_color(RED)
        remarque.shift([3,1.5,0])

        # Create dot A at the start of the curve
        initial_x_a = 1.5
        dot_a = Dot(ax.coords_to_point(initial_x_a, e**initial_x_a), color=RED)

        # Create dot B at coordinates (1, 1)
        dot_b = Dot(ax.coords_to_point(0.5, e**0.5), color=GREEN)

        # Position the labels next to the dots
        label_a.next_to(dot_a, RIGHT)
        label_b.next_to(dot_b, RIGHT)


        # Define the parabola curve
        parabola = ax.plot(lambda x: e**x, x_range=[-2, 7], use_smoothing=True)

        # Create a line initially passing through A and B
        def create_extended_line():
            # Calculate the direction vector from A to B
            direction = ax.point_to_coords(dot_b.get_center()) - ax.point_to_coords(dot_a.get_center())

            # Normalize the direction vector to unit length
            direction /= np.linalg.norm(direction)

            # Extend the line by a factor in both directions
            extension_factor = 2
            extended_start = ax.point_to_coords(dot_a.get_center()) - extension_factor * direction
            extended_end = ax.point_to_coords(dot_b.get_center()) + extension_factor * direction

            return Line(ax.coords_to_point(*extended_start), ax.coords_to_point(*extended_end), color=YELLOW)

        # Initialize the line
        line = create_extended_line()

        # Add updaters for the labels to follow the dots
        label_a.add_updater(lambda d: d.next_to(dot_a, RIGHT))
        label_b.add_updater(lambda d: d.next_to(dot_b, RIGHT))

        # Function to update dot A position along the curve
        def update_dot_a(dot, dt):
            # Get the current position of dot A
            current_x, current_y = ax.point_to_coords(dot.get_center())
            
            # Compute the new position for dot A
            new_x = current_x - 0.8*dt  # Move dot A leftward to move down the parabola
            new_y = e**new_x

            # Check if dot A is close to dot B
            if np.linalg.norm(ax.coords_to_point(new_x, new_y) - dot_b.get_center()) < 0.1:
                dot.remove_updater(update_dot_a)  # Stop moving if close to dot B
            else:
                dot.move_to(ax.coords_to_point(new_x, new_y))

        # Function to update the line to ensure it always passes through A and B
        def update_line(l):
            new_line = create_extended_line()
            l.become(new_line)

        # Initialize slope display
        slope = DecimalNumber(
            0,
            num_decimal_places=3,
            font_size=40
        )
        slope_title=Text("slope")
        slope.next_to(line)
        slope_title.next_to(slope,0.5*UP)
        approx=Tex(r"\[\cong e^{\frac{1}{2}}=f'(\frac{1}{2})\]")

        # Function to update the slope value
        def update_slope(slope_value):
            pos_a = ax.point_to_coords(dot_a.get_center())
            pos_b = ax.point_to_coords(dot_b.get_center())
            if pos_b[0] != pos_a[0]:  # Avoid division by zero
                slope.set_value((pos_b[1] - pos_a[1]) / (pos_b[0] - pos_a[0]))
            else:
                slope.set_value(float('inf'))

        # Add updaters to dot A, line, and slope
        line.add_updater(update_line)
        slope.add_updater(lambda d: d.next_to(line))
        slope.add_updater(update_slope)
        slope_title.add_updater(lambda d: d.next_to(slope,1*UP))

        # Add elements to the scene
        self.play(DrawBorderThenFill(ax), Create(parabola),Write(label_f))
        self.wait()
        self.play(Create(dot_a), Create(label_a))
        self.wait()
        self.play(Create(dot_b), Create(label_b),Create(remarque))
        self.wait()
        self.play(Create(line), Create(slope),Create(slope_title))
        self.wait(5)
        dot_a.add_updater(update_dot_a)
        self.wait(3)
        approx.next_to(slope)
        self.play(Write(approx))
        self.wait()
        dot_a.remove_updater(update_dot_a)
        line.remove_updater(update_line)
        slope.remove_updater(update_slope)
        # Clean up updaters
class web(Scene):
    def construct(self):
        math_text=Text("Math",font_size=80)
        math_text.set_color(RED)
        fun_text=Text("Fun",font_size=80)
        fun_text.set_color(GREEN)
        self.play(Write(math_text),run_time=1)
        self.wait(1)
        self.play(ReplacementTransform(math_text,fun_text),run_time=1)
        self.wait()
        
