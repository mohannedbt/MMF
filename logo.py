from manim import *
from math import*
class logo(Scene):
   def construct(self):
    title=Text("M.M.F",font_size=60)

    subtitle=Text("Where maths is actually fun !")
    subtitle.shift(2*DOWN)
    circle=Circle(stroke_color=WHITE,stroke_width=10).surround(title,buffer_factor=1.5)
    circle.set_color(BLUE)
    circle.set_opacity(0.5)
    self.play(DrawBorderThenFill(circle),Write(title),run_time=3)
    self.wait(0.5)
    self.play(title.animate.move_to(1.5*UP),circle.animate.move_to(1.5*UP))
    self.play(Write(subtitle),run_time=2.5)
    self.wait()
    self.play(FadeOut(title,subtitle,circle))

class Join(Scene):
    def construct(self):

        math_text=Text("MATH")
        math_rect=Rectangle(stroke_color=GREEN)
        math_rect.set_opacity(0.5)
        math_rect.set_color(GREEN)
        math_text.shift([-4,1,0])
        def update_rect(math_rect):
            math_rect.surround(math_text,buff=1.5)
        def update_rect2(fun_rect):
            fun_rect.surround(fun_text,buff=2)
        def update_math(math_text):
           math_text.next_to(a)
        def update_fun(fun_text):
           fun_text.next_to(b)
        fun_text=Text("FUN")
        fun_rect=Rectangle(stroke_color=BLUE)
        fun_rect.set_opacity(0.5)
        fun_rect.set_color(BLUE)
        fun_text.shift([4,1,0])
        funmath_text=Text("Math is Fun")
        funmath_rect=Rectangle(stroke_color=BLUE)
        funmath_rect.set_opacity(0.5)
        funmath_rect.set_color_by_gradient(BLUE,GREEN)
        funmath_text.shift([0,0,0])
        # Create dots for visualization
        a = Dot(point=[-6, 0, 0], color=BLUE)
        b = Dot(point=[4, 0, 0], color=RED)
        a.set_opacity(0)
        b.set_opacity(0)

        # Create a 2D arrow (adjusted to lie in the xy-plane)
        limits=Tex(r"\[\lim_{Math \to Fun} |math|-|fun|=\]",font_size=60)
        limits.shift(2*DOWN,1*LEFT)
        arrow = Arrow(start=a.get_center(), end=b.get_center())
        arrow.set_opacity(0)
        decimal = DecimalNumber(
            arrow.get_length(),
            show_ellipsis=True,
            num_decimal_places=3,
            unit_buff_per_font_unit=0.003,
            color=RED,
            font_size=60
        )
        decimal.next_to(limits)
        # Updater function to keep the arrow connected to the dots
        def update_arrow(arrow):
               arrow.put_start_and_end_on(a.get_center(), b.get_center())
        decimal.add_updater(lambda d: d.set_value(arrow.get_length()))
        # Add the updater to the arrow
        arrow.add_updater(update_arrow)
        math_text.add_updater(update_math)
        math_rect.add_updater(update_rect)
        fun_rect.add_updater(update_rect2)
        fun_text.add_updater(update_fun)
        

        # Add objects to the scene
        self.play(Create(a), Create(b),Create(math_rect),Write(math_text),run_time=1)
        self.play(Create(fun_rect),Write(fun_text),run_time=1)
        self.play(Create(decimal), Create(arrow),Create(limits),run_time=1)
        self.wait(1)

        # Animate moving dot 'a' to a new location
        self.play(a.animate.move_to([0, 0, 0]),b.animate.move_to([0,0,0]))
        self.remove(math_rect,fun_rect)
        self.play(ReplacementTransform(math_text,funmath_text),ReplacementTransform(fun_text,funmath_text),Create(funmath_rect))

        # Wait to view the result
        self.wait(2)