import numpy as np
from manim import *

from manim_slides import *

CURSOR_COLOR = PURE_GREEN
CURSOR_BLINK_TIME = 0.2

def type_text(self, text_mobject, blink_before=1, blink_after=1, total_time=0.5):
    """
    Animates the text appearing character by character with a blinking cursor.
    """
    
    cursor_width = text_mobject[0].width
    cursor_height = text_mobject.height * 0.1
    cursor = Rectangle(
        height=cursor_height,
        width=cursor_width,
        color=CURSOR_COLOR,
        fill_opacity=1
    )

    initial_cursor_x = text_mobject.get_critical_point(LEFT)[0] + cursor_width / 2
    initial_cursor_y = text_mobject.get_critical_point(DOWN)[1]
    cursor.move_to(np.array([initial_cursor_x, initial_cursor_y, 0]))

    self.play(
        FadeIn(cursor),
        run_time=0.05 # Halved
    )
    self.wait(CURSOR_BLINK_TIME)
    for _ in range(blink_before):
        self.play(
            FadeOut(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)
        self.play(
            FadeIn(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)

    time_per_letter = total_time / len(text_mobject)
    target_y = text_mobject.get_critical_point(DOWN)[1]

    for letter in text_mobject:
        target_x = letter.get_right()[0] + cursor_width / 2
        target_cursor_pos = np.array([target_x, target_y, 0])

        self.play(
            cursor.animate.move_to(target_cursor_pos),
            FadeIn(letter),
            run_time=time_per_letter
        )
        self.wait(0.05)
        
    for _ in range(blink_after):
        self.play(
            FadeOut(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)
        self.play(
            FadeIn(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)
        
    self.play(
        FadeOut(cursor),
        run_time=0.1 # Halved
    )
        

class Welcome(Slide):
    def construct(self):
        title = Text("Linux Workshop", color=PURE_GREEN, font_size=100, font="CaskaydiaCove Nerd Font")

        type_text(self, title)

class WhatIsLinux(Slide):
    def construct(self):
        prompt = Text("[linux-workshop@ECE ~]$ ", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        prompt.move_to(UP * 2 + LEFT * 2.5)
        self.play(
            AddTextLetterByLetter(prompt, run_time=0.3)
        )
        
        command = Text("cat what_is_linux", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        command.next_to(prompt, RIGHT)
        type_text(self, command, blink_before=3, total_time=0.3)

        title = Text("What is Linux?", color=BLUE, font_size=100, font="CaskaydiaCove Nerd Font")
        self.play(
            AddTextLetterByLetter(title, run_time=0.3)
        )

        kernel = Text("# Linux Kernel", color=YELLOW, font_size=30, font="CaskaydiaCove Nerd Font")
        kernel.next_to(title, DOWN, buff=LARGE_BUFF).align_to(title, LEFT)
        self.play(
            Write(kernel, run_time=0.5)
        )

        kernel_text_lines_str = [
            "- The core of Linux OS",
            "- Manages hardware resources",
            "- Open source",
            "- Introduced in 1991 by Linus Torvalds"
        ]

        elements_on_screen = VGroup(prompt, command, title, kernel)
        kernel_lines_mobjects = VGroup()

        sample_line = Text("X", color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font")
        line_height = sample_line.height * 2.25

        for i, line_str in enumerate(kernel_text_lines_str):
            self.play(elements_on_screen.animate.shift(UP * line_height), run_time=0.2)

            current_line = Text(line_str, color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font")
            if i == 0:
                current_line.next_to(kernel, DOWN, aligned_edge=LEFT, buff=0.25)
            else:
                current_line.next_to(kernel_lines_mobjects[-1], DOWN, aligned_edge=LEFT, buff=0.25)

            self.play(Write(current_line, run_time=0.4))

            elements_on_screen.add(current_line)
            kernel_lines_mobjects.add(current_line)

        self.wait(0.5)

        self.next_slide(auto_next=True)

        # Add final prompt
        self.play(elements_on_screen.animate.shift(UP * line_height), run_time=0.2)
        final_prompt = Text("[linux-workshop@ECE ~]$ ", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        # Position below the last kernel line
        final_prompt.next_to(kernel_lines_mobjects[-1], DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(
            AddTextLetterByLetter(final_prompt, run_time=0.3)
        )
        elements_on_screen.add(final_prompt)

        cursor = Rectangle(
            height=final_prompt.height * 0.1,
            width=final_prompt[0].width,
            color=CURSOR_COLOR,
            fill_opacity=1
        )
        cursor.next_to(final_prompt, RIGHT + cursor.height * DOWN, buff=0.1)

        self.next_slide(loop=True)

        self.play(
            FadeIn(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)
        self.play(
            FadeOut(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)

        self.next_slide()

        mpv_1 = Text("mpv 'https://www.youtu", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        mpv_1.next_to(final_prompt, RIGHT)
        type_text(self, mpv_1, blink_before=3, blink_after=0, total_time=0.3)

        elements_on_screen.add(mpv_1)
        self.play(elements_on_screen.animate.shift(UP * line_height), run_time=0.2)

        mpv_2 = Text("be.com/watch?v=OF_5EKNX0Eg'", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        mpv_2.next_to(final_prompt, DOWN, aligned_edge=LEFT)
        type_text(self, mpv_2, blink_before=0, blink_after=2, total_time=0.3)

        elements_on_screen.add(mpv_2)

        self.wait(1)

        self.play(elements_on_screen.animate.shift(UP * line_height), run_time=0.2)

class LinuxDistro(Slide):
    def construct(self):
        prompt = Text("[linux-workshop@ECE ~]$ ", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        prompt.move_to(UP * 2 + LEFT * 2.75)
        self.add(prompt)

        mpv_1 = Text("mpv 'https://www.youtu", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        mpv_1.next_to(prompt, RIGHT)
        self.add(mpv_1)

        mpv_2 = Text("be.com/watch?v=OF_5EKNX0Eg'", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        mpv_2.next_to(prompt, DOWN, aligned_edge=LEFT)
        self.add(mpv_2)

        terminal_output = VGroup(
            Text("AO: [pipewire] 48000Hz stereo 2ch floatp", color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font"),
            Text("VO: [gpu] 1920x1080 yuv420p", color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font"),
            Text("AV: 00:00:13 / 00:00:13 (99%) A-V:  0.000 Ca...", color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font"),
            Text("Exiting... (End of file)", color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font"),
        )
        # Arrange the text elements vertically, aligned to the left
        terminal_output.arrange(DOWN, aligned_edge=LEFT, buff=0.25) # Adjust buff for desired line spacing

        terminal_output.next_to(prompt, DOWN * 3.5, aligned_edge=LEFT) # Position below the second line of mpv output
        self.add(terminal_output)

        self.wait()

        # Combine all elements currently on screen for easier animation
        elements_on_screen = VGroup(prompt, mpv_1, mpv_2, terminal_output)

        sample_line = Text("X", color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font")
        line_height = sample_line.height * 2.25

        # Add final prompt
        final_prompt = Text("[linux-workshop@ECE ~]$ ", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        final_prompt.next_to(terminal_output[-1], DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(
            AddTextLetterByLetter(final_prompt, run_time=0.3)
        )
        elements_on_screen.add(final_prompt)

        # Type the command
        command = Text("cat linux_distro", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        command.next_to(final_prompt, RIGHT)
        type_text(self, command, blink_before=3, total_time=0.3)
        elements_on_screen.add(command)

        # Add the title and description lines
        distro_text_lines_str = [
            "# Linux Distribution (Distro)",
            "- A software pack including the kernel",
            "- Contains components, utilities, apps, etc.",
            "- Use package manager (apt, pacman, dnf, etc.)",
            "Popular distros: Ubuntu, Arch, Debian, Fedora,",
            "Linux Mint, RHEL, Kali Linux, and many more"
        ]

        distro_lines_mobjects = VGroup()

        for i, line_str in enumerate(distro_text_lines_str):
            self.play(elements_on_screen.animate.shift(UP * line_height), run_time=0.2)

            current_line = Text(line_str, color=WHITE, font_size=30, font="CaskaydiaCove Nerd Font")
            if i == 0: # Title line, position below command
                current_line.next_to(final_prompt, DOWN, aligned_edge=LEFT, buff=0.25)
                current_line.set_color(YELLOW) # Set title color
            else:
                current_line.next_to(distro_lines_mobjects[-1], DOWN, aligned_edge=LEFT, buff=0.25)

            self.play(Write(current_line, run_time=0.4))

            elements_on_screen.add(current_line)
            distro_lines_mobjects.add(current_line)

        self.wait(0.5)

        self.next_slide(auto_next=True)

        # Add final prompt after content
        self.play(elements_on_screen.animate.shift(UP * line_height), run_time=0.2)
        end_prompt = Text("[linux-workshop@ECE ~]$ ", color=PURE_GREEN, font_size=30, font="CaskaydiaCove Nerd Font")
        # Position below the last distro line
        end_prompt.next_to(distro_lines_mobjects[-1], DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(
            AddTextLetterByLetter(end_prompt, run_time=0.3)
        )
        elements_on_screen.add(end_prompt)

        cursor = Rectangle(
            height=end_prompt.height * 0.1,
            width=end_prompt[0].width,
            color=CURSOR_COLOR,
            fill_opacity=1
        )
        cursor.next_to(end_prompt, RIGHT + cursor.height * DOWN, buff=0.1)

        self.next_slide(loop=True)

        self.play(
            FadeIn(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)
        self.play(
            FadeOut(cursor),
            run_time=0.05 # Halved
        )
        self.wait(CURSOR_BLINK_TIME)

        self.next_slide()

        self.wait() # Keep the final state visible