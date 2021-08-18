from manim import *


class Animation(Scene):

    def animalist(f1, f2):
        a = []
        for i in range(len(f1)):
            for j in range(len(f2)):
                if f1[i].get_tex_string() == f2[j].get_tex_string():
                    a.append([i, j])
        return a

    def isnotani(j, arr):
        return j in arr

    def DespejeEqt(f1, f2, fi=FadeIn, fo=FadeOut, lr=0):
        a = [f1[i].animate.move_to(f2[j]) for i, j in Animation.animalist(f1, f2)] + [
            fi(f2[i], shift=DOWN) for i in range(len(f2)) if not Animation.isnotani(i, [j for i, j in Animation.animalist(f1, f2)])
        ] + [
            fo(f1[i], shift=DOWN) for i in range(len(f1)) if not Animation.isnotani(i, [i for i, j in Animation.animalist(f1, f2)])
        ]

        return AnimationGroup(*a, lag_ratio=lr)
    
    def NewEq(this,*keys):
        this.clear()
        this.add(*keys)
    
    def AnimatedList(this,eqs):
        for i in range(len(eqs)-1):
            this.play(
                Animation.DespejeEqt(eqs[i],eqs[i+1]),
                run_time=2
            )
            Animation.NewEq(this,eqs[i+1])
            this.wait(2)
    
    def CleanFO(this,*v):
        this.play(
            FadeOut(VGroup(*v)),
            run_time=0.5
        )
        this.wait(1.5)
