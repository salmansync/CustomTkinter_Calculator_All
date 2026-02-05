import customtkinter as ctk
import tkinter.messagebox as mbox
import re
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
# Test

        icon_path = r"C:\Users\Salman Farsi\Documents\Project\CustomTkinter_Calculator_All\Project\calculator_icon.ico"
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        else:
            print("Icon file not found:", icon_path)

        self.title("Calculator")
        self.geometry("350x650")
        self.maxsize(400, 750)
        self.minsize(350, 650)

        self.expression = ""
        self.last_result = ""
        self.is_dark_mode = True
        self.history_shown = False
        self.max_input_length = 100

        self.create_widgets()
        self.bind("<Key>", self.handle_keypress)
    def create_widgets(self):
        self.display_box = ctk.CTkTextbox(self, height=100, font=('Segoe UI', 36), activate_scrollbars=False, wrap="none")
        self.display_box.insert("1.0", "")
        self.display_box.configure(state="disabled")
        self.display_box.pack(fill='x', padx=10, pady=(10, 5))
        self.display_box.bind("<Button-1>", self.copy_result_to_clipboard)

        self.history_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.history_box = ctk.CTkTextbox(self.history_frame, height=90, font=('Consolas', 20), fg_color="transparent",
                                          text_color="#999999", activate_scrollbars=False, wrap="none")
        self.history_box.pack(fill='both', expand=True)
        self.history_box.configure(state="disabled")

        self.top_row = ctk.CTkFrame(self, fg_color="transparent")
        self.top_row.pack(fill='x', pady=(5, 5))

        self.btn_style = {'font': ('Segoe UI', 18), 'height': 40, 'corner_radius': 10, 'width': 80}

        self.history_btn = ctk.CTkButton(self.top_row, text="History", command=self.toggle_history_view, **self.btn_style)
        self.history_btn.pack(side='left', padx=(10, 5))

        self.clear_history_btn = ctk.CTkButton(self.top_row, text="Clear", command=self.clear_history, **self.btn_style)
        self.clear_history_btn.pack_forget()

        self.theme_btn = ctk.CTkButton(self.top_row, text="☀️ Light", command=self.flip_theme, **self.btn_style)
        self.theme_btn.pack(side='right', padx=(5, 10))

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand=True)

        self.build_buttons()

    def build_buttons(self):
        self.frame.destroy()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand=True)

        def get_color_settings(text):
            white = "#ffffff"
            black = "#000000"
            red = "#d00000"
            dark_bg = "#2c2c2c"
            hover = "#dcdcdc" if not self.is_dark_mode else "#3a3a3a"

            if text in ('C', '⌫'):
                return {'fg_color': red, 'text_color': white, 'hover_color': hover}
            elif text in ('+', '-', '×', '÷'):
                return {'fg_color': black, 'text_color': white, 'hover_color': hover}
            else:
                return {
                    'fg_color': white if not self.is_dark_mode else dark_bg,
                    'text_color': black if not self.is_dark_mode else white,
                    'hover_color': hover
                }

        buttons = [
            ('√', self.do_square_root), ('^', lambda: self.press_key('^')), ('C', self.clear_all), ('⌫', self.delete_last),
            ('(', lambda: self.press_key('(')), (')', lambda: self.press_key(')')), ('%', self.do_percentage), ('÷', lambda: self.press_key('÷')),
            ('7', lambda: self.press_key('7')), ('8', lambda: self.press_key('8')), ('9', lambda: self.press_key('9')), ('×', lambda: self.press_key('×')),
            ('4', lambda: self.press_key('4')), ('5', lambda: self.press_key('5')), ('6', lambda: self.press_key('6')), ('-', lambda: self.press_key('-')),
            ('1', lambda: self.press_key('1')), ('2', lambda: self.press_key('2')), ('3', lambda: self.press_key('3')), ('+', lambda: self.press_key('+')),
            ('ANS', self.insert_ans), ('0', lambda: self.press_key('0')), ('.', lambda: self.press_key('.')), ('=', self.evaluate),
        ]

        for idx, (txt, cmd) in enumerate(buttons):
            colors = get_color_settings(txt)
            btn = ctk.CTkButton(self.frame, text=txt, command=cmd, **self.btn_style, **colors)
            btn.grid(row=idx // 4, column=idx % 4, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.frame.grid_rowconfigure(i, weight=1)

        for btn in [self.history_btn, self.clear_history_btn, self.theme_btn]:
            colors = get_color_settings(btn.cget("text"))
            btn.configure(**colors)

    def get_display_font_size(self):
        length = len(self.expression)
        if length <= 10:
            return ('Segoe UI', 36)
        elif length <= 20:
            return ('Segoe UI', 28)
        elif length <= 30:
            return ('Segoe UI', 22)
        else:
            return ('Segoe UI', 16)

    def update_display(self):
        self.display_box.configure(state="normal")
        self.display_box.delete("1.0", "end")
        self.display_box.insert("1.0", self.expression)
        self.display_box.configure(font=self.get_display_font_size())
        self.display_box.configure(state="disabled")

    def press_key(self, val):
        if len(self.expression) >= self.max_input_length:
            mbox.showwarning("Limit", "Maximum input length reached!")
            return

        operators = "+-×÷^"
        if val in operators:
            if not self.expression:
                return
            if self.expression[-1] in operators:
                self.expression = self.expression[:-1]
            self.expression += val
            self.update_display()
            return

        self.expression += val
        self.update_display()

    def evaluate(self):
        try:
            expr = self.expression.replace('÷', '/').replace('×', '*').replace('^', '**')
            if self.last_result:
                expr = expr.replace('ANS', self.last_result)

            expr = re.sub(r'\b0+(\d)', r'\1', expr)

            result = eval(expr)
            self.last_result = str(result)
            rounded = round(result, 2)
            result_display = int(rounded) if rounded == int(rounded) else rounded

            self.history_box.configure(state="normal")
            self.history_box.insert("end", f"{self.expression} = {result_display}\n")
            self.history_box.configure(state="disabled")

            self.expression = str(result_display)
            self.update_display()
        except ZeroDivisionError:
            self.expression = "Can't divide by zero"
            self.update_display()
            self.expression = ""
        except Exception:
            self.expression = "Error"
            self.update_display()
            self.expression = ""

    def clear_all(self):
        self.expression = ""
        self.update_display()

    def delete_last(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def do_square_root(self):
        try:
            if not self.expression:
                return
            expr = self.expression.replace('÷', '/').replace('×', '*').replace('^', '**')
            if self.last_result:
                expr = expr.replace('ANS', self.last_result)
            val = eval(expr)
            if val < 0:
                raise ValueError("Invalid Input")

            sqrt_val = val ** 0.5
            rounded = round(sqrt_val, 2)
            result_display = int(rounded) if rounded == int(rounded) else rounded
            self.last_result = str(result_display)
            self.expression = self.last_result

            self.update_display()

            self.history_box.configure(state="normal")
            self.history_box.insert("end", f"√({val}) = {result_display}\n")
            self.history_box.configure(state="disabled")

        except:
            self.expression = "Error"
            self.update_display()
            self.expression = ""

    def do_percentage(self):
        try:
            if not self.expression:
                return
            expr = self.expression.replace('×', '*').replace('÷', '/').replace('^', '**')
            if self.last_result:
                expr = expr.replace('ANS', self.last_result)
            original = self.expression + '%'
            for op in "+-*/":
                if op in expr:
                    parts = expr.rsplit(op, 1)
                    if len(parts) == 2:
                        left = float(parts[0])
                        right = float(parts[1])
                        res = {
                            '+': left + (left * right / 100),
                            '-': left - (left * right / 100),
                            '*': left * (right / 100),
                            '/': left / (right / 100) if right != 0 else float('inf')
                        }[op]
                        break
            else:
                res = float(expr) / 100
            self.last_result = str(res)
            final = round(res, 2)
            final = int(final) if final == int(final) else final
            self.expression = str(final)
            self.update_display()
            self.history_box.configure(state="normal")
            self.history_box.insert("end", f"{original} = {final}\n")
            self.history_box.configure(state="disabled")
        except:
            self.expression = "Error"
            self.update_display()
            self.expression = ""

    def toggle_history_view(self):
        self.history_shown = not self.history_shown
        if self.history_shown:
            self.history_frame.pack(after=self.display_box, fill='both', expand=False, padx=10, pady=(5, 5))
            self.clear_history_btn.pack(side='left', padx=5)
        else:
            self.history_frame.pack_forget()
            self.clear_history_btn.pack_forget()

    def flip_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        mode = "dark" if self.is_dark_mode else "light"
        self.theme_btn.configure(text="☀️ Light" if mode == "dark" else "🌙 Dark")
        ctk.set_appearance_mode(mode)

        if self.history_shown:
            self.history_frame.pack_forget()
            self.clear_history_btn.pack_forget()

        self.build_buttons()

        if self.history_shown:
            self.history_frame.pack(after=self.display_box, fill='both', expand=False, padx=10, pady=(5, 5))
            self.clear_history_btn.pack(side='left', padx=5)

    def clear_history(self):
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        self.history_box.configure(state="disabled")

    def insert_ans(self):
        if self.last_result:
            self.press_key(self.last_result)

    def handle_keypress(self, evt):
        key = evt.char
        sym = evt.keysym

        if key in '0123456789.+-*/()':
            self.press_key(key.replace('*', '×').replace('/', '÷'))
        elif key.lower() == 'a':
            self.press_key("ANS")
        elif key == '\r':
            self.evaluate()
        elif sym == 'BackSpace':
            self.delete_last()
        elif sym == 'Escape':
            self.clear_all()
        elif key == '^':
            self.press_key('^')
        elif key == '%':
            self.do_percentage()
        elif key.lower() == 'r':
            self.do_square_root()
        elif sym.lower() == 't':
            self.flip_theme()

    def copy_result_to_clipboard(self, event):
        self.clipboard_clear()
        self.clipboard_append(self.expression)
        self.update()


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
