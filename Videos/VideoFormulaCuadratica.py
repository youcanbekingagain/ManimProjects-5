from manim import *
import math as m


class Portada(Scene):
    def construct(self):

        f = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"
        ).set_color_by_gradient(YELLOW, RED, GREEN).scale(2.2)

        self.add(f)


class IntroduccionFormulaCuadratica(Scene):
    def construct(self):

        texto1 = Title(
            'Formula Cuadrática'
        ).scale(1.1)

        texto1.set_color(YELLOW_C)

        texto2 = Text(
            r"""
            ¿Sabes de donde viene esta fórmula?
            
            Te enseñare :)
            """
        ).scale(0.6)

        self.play(
            Write(texto1),
            run_time=3
        )
        self.wait(2)
        
        self.play(
            Write(texto2),
            run_time=2
        )
        self.wait()


class FuncionesCuadraticas(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-5, 5], y_range=[-10, 10, 1], axis_config={"include_tip": False, "stroke_width": 5}
        )
        
        Titulo = MarkupText(
            f"Algunos ejemplos de funciones <span fgcolor='{RED}'>Cuadráticas</span>"
        ).scale(.5).to_corner(UL)

        ecuacionA = ax.get_graph(lambda x: (
            x+1)*(x-1), x_range=[-m.sqrt(10), m.sqrt(10)], color=RED)
        ecuacionB = ax.get_graph(
            lambda x: x*(x-2), x_range=[-m.sqrt(4), 4], color=GREEN)
        ecuacionC = ax.get_graph(
            lambda x: -0.5*(x+5)*(x-PI), x_range=[-5, 5], color=BLUE)
        
        ec1 = MathTex(
            r"f(x) = x^2 - 1"
        ).scale(.6).set_color(RED).to_corner(UR)
        
        ec2 = MathTex(
            r"f(x) = x^2 - 2x"
        ).scale(.6).set_color(GREEN).to_corner(UR)
        
        ec3 = MathTex(
            r"f(x) = -\frac{x^2}{2} +\frac{\pi}{2} x - \frac{5}{2}x +\frac{5\pi}{2}"
        ).scale(.6).set_color(BLUE).to_corner(UR)

        self.play(
            LaggedStart(
                Write(ax),
                Write(Titulo),
                Write(ec1),
                Write(ecuacionA),
                lag_ratio=1.2
            )
        )

        self.play(
            Succession(
                Transform(ec1,ec2),
                Transform(ecuacionA, ecuacionB),
                Transform(ec1,ec3),
                Transform(ecuacionA, ecuacionC),
                lag_ratio=1.2
            )
        )
        self.wait()


class EcuacionesSoluciones(Scene):
    def construct(self):

        def animatez(f1, f2):
            a = []
            for i in range(len(f1)):
                for j in range(len(f2)):
                    if f1[i].get_tex_string() == f2[j].get_tex_string():
                        a.append([i, j])

            return a

        def isnotani(j, arr):
            return j in arr
        
        def Despeanieq(f1,f2,lr=0):
            a = [f1[i].animate.move_to(f2[j]) for i, j in animatez(f1, f2)] + [
                FadeIn(f2[i],shift=DOWN) for i in range(len(f2)) if not isnotani(i, [j for i, j in animatez(f1, f2)])
            ] + [
                FadeOut(f1[i],shift=DOWN) for i in range(len(f1)) if not isnotani(i, [i for i, j in animatez(f1, f2)])
            ]
            
            return AnimationGroup(*a,lag_ratio=lr)
        
        def NewEq(*keys):
            self.clear()
            self.add(*keys)
            
        Titulo = MarkupText(
            f"<span fgcolor='{GREEN}'>Desarrollo</span>"
        ).scale(1.2).to_corner(UL)

        f1 = MathTex(
            "a","x^2","+","b","x","+","c","=","0"
        )

        self.play(
            Create(f1),
            Write(Titulo),
            run_time=3
        )
        self.wait(2)

        f2 = MathTex(
            "a","x^2","+","b","x","=","-c"
        )
        
        f3 = MathTex(
            "\\frac{1}{a}\\left(","a","x^2","+","b","x","=","-c","\\right)"
        )
        
        f4 = MathTex(
            "x^2","+","\\frac{b}{a}","x","=","-","\\frac{c}{a}"
        )
        
        f5 = MathTex(
            "x^2","+","\\frac{b}{a}","x","+","\\frac{b^2}{4a^2}","=","-","\\frac{c}{a}","+","\\frac{b^2}{4a^2}"
        )
        
        f6 = MathTex(
            "\\left(","x","+","\\frac{b}{2a}","\\right)^2","=","-","\\frac{c}{a}","+","\\frac{b^2}{4a^2}"
        )
        
        f7 = MathTex(
            "\\left(","x","+","\\frac{b}{2a}","\\right)^2","=","\\frac{b^2}{4a^2}","-","\\frac{c}{a}"
        )
        
        f8 = MathTex(
            "\\left(","x","+","\\frac{b}{2a}","\\right)^2","=","\\frac{b^2}{4a^2}","-","\\frac{c}{a}","\\frac{4a}{4a}"
        )
        
        f9 = MathTex(
            "\\left(","x","+","\\frac{b}{2a}","\\right)^2","=","\\frac{b^2}{4a^2}","-","\\frac{4ac}{4a^2}"
        )
        
        f10 = MathTex(
            "\\left(","x","+","\\frac{b}{2a}","\\right)^2","=","\\frac{b^2 - 4ac}{4a^2}"
        )
        
        f11 = MathTex(
            "x","+","\\frac{b}{2a}","=","\\pm","\\sqrt{","\\frac{b^2 - 4ac}{4a^2}","}"
        )
        
        f12 = MathTex(
            "x","=","-","\\frac{b}{2a}","\\pm","\\sqrt{","\\frac{b^2 - 4ac}{4a^2}","}"
        )
        
        f13 = MathTex(
            "x","=","-","\\frac{b}{2a}","\\pm","\\frac{\\sqrt{b^2 - 4ac}}{","\\sqrt{4a^2}}"
        )
        
        f14 = MathTex(
            "x","=","-","\\frac{b}{2a}","\\pm","\\frac{\\sqrt{b^2 - 4ac}}{","2a}"
        )
        
        f15 = MathTex(
            "x","=","\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        ).set_color_by_gradient(YELLOW,BLUE,GREEN)
        
        n1 = MathTex(
            "x_0","=","\\frac{-b + \\sqrt{b^2 - 4ac}}{2a}"
        )
        
        n2 = MathTex(
            "x_1","=","\\frac{-b - \\sqrt{b^2 - 4ac}}{2a}"
        )
        
        n3 = MathTex(
            "ax^2 + bx + c =","a(x-","x_0",")(x-","x_1",")"
        )
        
        self.add(Titulo)
        
        eqs = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]
        
        for i in range(len(eqs)-1):
            self.play(
                Despeanieq(eqs[i],eqs[i+1]),
                run_time=2
            )
            NewEq(eqs[i+1],Titulo)
            self.wait(2)
            
        self.play(
            FadeOut(f15),
            FadeIn(n1),
            FadeIn(n2),
            n1.animate.shift(UP),
            n2.animate.shift(DOWN),
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(n1[1:]),
            FadeOut(n2[1:]),
        )
        
        self.wait(2)
        
        self.play(
            n1[0].animate.move_to(n3[2]),
            n2[0].animate.move_to(n3[4]),
            Write(n3)
        )
        
        self.play(
            ShowCreationThenFadeOut(SurroundingRectangle(mobject=n3,color=YELLOW,buff=.15)),
            run_time=5
        )
        
        self.wait(3)
        
        
class Final(Scene):
    def construct(self):
        
        F = Text("Gracias por ver.").scale(1.3).set_color_by_gradient(BLUE_B,GREEN_D,PURPLE_B)
        
        self.play(
            FadeIn(F,shift=UP),
            run_time=4
        )
