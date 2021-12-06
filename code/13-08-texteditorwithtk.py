#%% Mini Project 8 13-08-texteditorwithtk.py
# os.path.basename 사용
import os
# 기본적인 위젯 Frame, Text, Menu등 사용
from tkinter import *
# 파일 열기, 다른 이름으로 저장, 메시지막스 등 대화상자 사용
from tkinter import filedialog, messagebox

class TextEditor():
    '''테스트 편집기'''
    def __init__(self, root):
        self.root = root
        self.TITLE = "TkInter 편집기"
        #작업 중인 파일 이름을 저장 
        self.file_path = None
        #초기 윈도 캡션을 Untitled로 지정
        self.set_title()

        frame = Frame(root)
        # 세로 스크롤바를 생성
        self.yscrollbar = Scrollbar(frame, orient="vertical")
        # 세로 스크롤바를 연결하여 기본 편집을 지원하는 위젯 Text 생성
        self.editor = Text(frame, yscrollcommand=self.yscrollbar.set)
        # 스크롤 바의 이벤트를 위젯 Text의 yview에 설정
        self.yscrollbar.config(command=self.editor.yview)
        # 스크롤 바 배치
        self.yscrollbar.pack(side="right", fill="y")

        # Text 편집기 배치
        self.editor.pack(side="left", fill="both", expand=1)
        # Text 편집기 설정
        self.editor.config(wrap="word", undo=True, width=80)
        self.editor.focus()
        frame.pack(fill="both", expand=1)

        # 윈도 종료 버튼을 메소드 file_quit으로 전달
        root.protocol("WM_DELETE_WINDOW", self.file_quit)
        # 메뉴 생성
        self.make_menu()
        # 단축키 이벤트를 메소드와 연결
        self.bind_events()

    def make_menu(self):
        # 메뉴의 최상위인 메뉴바 생성
        self.menubar = Menu(root)

        # 메뉴 아이템 File
        fmenu = Menu(self.menubar, tearoff=0)  # tearoff = 0 윈도에 분리되지 않도록 설정
        fmenu.add_command(label="New", command=self.file_new, accelerator="Ctrl+N")
        fmenu.add_command(label="Open...", command=self.file_open, accelerator="Ctrl+O")
        fmenu.add_command(label="Save", command=self.file_save, accelerator="Ctrl+S")
        fmenu.add_command(label="Save As...", command=self.file_save_as, accelerator="Ctrl+Alt+S")
        fmenu.add_separator() # 중간 구분자 추가 
        fmenu.add_command(label="Exit", command=self.file_quit, accelerator="Alt+F4")
        # 메뉴바에 File을 추가
        self.menubar.add_cascade(label="File", menu=fmenu)

        # 메뉴 아이템 Edit
        emenu = Menu(self.menubar, tearoff=0)
        emenu.add_command(label="Cut", command=self.edit_cut)
        emenu.add_command(label="Copy", command=self.edit_copy)
        emenu.add_command(label="Paste", command=self.edit_paste)
        # 메뉴바에 Edit를 추가
        self.menubar.add_cascade(label="Edit", menu=emenu)

        # 메뉴 아이템 Help
        hmenu = Menu(self.menubar, tearoff=0)
        hmenu.add_command(label="TkEditor 편집기", command=self.help_showabout)
        # 메뉴바에 Help를 추가
        self.menubar.add_cascade(label="Help", menu=hmenu)

        # 메뉴 보이기
        root.config(menu=self.menubar)

    def save_if_modified(self):
        # editor가 수정되었다면 다시 저장하도록 사용자에게 메시지 박스로 질의 
        if self.editor.edit_modified():  
            caption = '저장 확인'
            msg = '이 파일은 수정되었습니다. 저장하시겠습니까?'
            # yes = True, no = False, cancel = None
            response = messagebox.askyesnocancel(caption, msg)  
            if response:  # 저장하도록 저장 메소드 호출
                result = self.file_save()
                if result == "saved":  # 저장 완료
                    return True
                else:  # 저장 취소
                    return None
            else:
                return response  # None = cancel/abort, False = no/discard
        else:  # 수정되지 않았으면
            return True

    def file_new(self, event=None):
        # 이전 파일이 있다면 먼저 저장하도록
        result = self.save_if_modified()
        if result != None:  # 무시하거나 파일이 저장되었다면, 새로운 파일을 편집 준비
            #편집기 내용을 모두 삭제, 1.0은 첫 번째 줄, 첫 번째 문자를 가리키며, 'end'는 끝
            self.editor.delete(1.0, "end")
            self.editor.edit_modified(False)
            self.editor.edit_reset()
            self.file_path = None
            self.set_title()

    def file_open(self, event=None, filepath=None):
        def readfile(filepath):
            try:
                with open(filepath, encoding="utf-8") as f:
                    fileContents = f.read()  # 파일에서 모든 내욜을 읽어 오기
            except FileNotFoundError as e:
                print(e)
                print(' 파일 읽기 실패! '.center(30, '*'))
            else:
                # 읽어온 내용을 위젯 Text에 모두 삽입
                self.editor.delete(1.0, "end")  # 먼저 이전 내용 모두 삭제
                self.editor.insert(1.0, fileContents)  # 읽어온 내용 모두 삽입
                self.editor.edit_modified(False)
                self.file_path = filepath
                print(' 파일 읽기 완료! '.center(30, '*'))

        result = self.save_if_modified()
        if result != None:  # 무시하거나 파일이 저장되었다면, 새로운 파일 열기 준비
            if filepath == None:
                filepath = filedialog.askopenfilename()
            if filepath != None and filepath != '':
                readfile(filepath)
                self.set_title()

    def file_save(self, event=None):
        if self.file_path == None:
            result = self.file_save_as()
        else:
            result = self.file_save_as(filepath=self.file_path)
        return result

    def file_save_as(self, event=None, filepath=None):
        if filepath == None:
            ftypes = (('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*'))
            filepath = filedialog.asksaveasfilename(filetypes = ftypes)  # 기본은 첫 항목인 '.txt'

        # Text에서 모든 내용 가져오기
        text = self.editor.get(1.0, "end-1c")  # 마지막의 \n(new line)문자 문자를 제외하고
        try:
            with open(filepath, 'wb') as f:
                f.write(bytes(text, 'UTF-8'))
        except FileNotFoundError as e:
            print(e)
            print(' 파일 쓰기 실패! '.center(30, '*'))
            return "cancelled"
        else:
            self.editor.edit_modified(False)
            self.file_path = filepath
            self.set_title()
            return "saved"

    def file_quit(self, event=None): 
        '''종료 버튼이나 메뉴 Exit을 선택하면 실행'''
        result = self.save_if_modified()
        if result != None:  # 기존 편집하던 것이 해결되었으면
            self.root.destroy()  # sys.exit(0)

    def edit_cut(self, event=None):
        self.editor.event_generate("<<Cut>>")

    def edit_copy(self, event=None):
        self.editor.event_generate("<<Copy>>")

    def edit_paste(self, event=None):
        self.editor.event_generate("<<Paste>>")

    def help_showabout(self, event=None):
        messagebox.showinfo('TkInter 편집기', 'TkInter 편집기 버전 0.1')

    def set_title(self, event=None):
        if self.file_path != None:
            # 파일의 기본 이름을 반환
            title = os.path.basename(self.file_path)
        else:
            title = "Untitled"
        self.root.title(title + " - " + self.TITLE)

    def undo(self, event=None):
        self.editor.edit_undo()

    def redo(self, event=None):
        self.editor.edit_redo()

    def bind_events(self, event=None):
        self.editor.bind("<Control-o>", self.file_open)
        self.editor.bind("<Control-O>", self.file_open)
        self.editor.bind("<Control-S>", self.file_save)
        self.editor.bind("<Control-s>", self.file_save)
        self.editor.bind("<Control-y>", self.redo)
        self.editor.bind("<Control-Y>", self.redo)
        self.editor.bind("<Control-Z>", self.undo)
        self.editor.bind("<Control-z>", self.undo)

root = Tk()
root.geometry('800x600')
# root를 부모로 TextEditor 객체 생성
editor = TextEditor(root)
root.mainloop()
