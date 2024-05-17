'''
Author: 木白广木林
Date: 2024-05-16 16:47:37
LastEditTime: 2024-05-17 10:16:08
LastEditors: 木白广木林
Description: None
FilePath: \Desktop\db.py
检查自己的代码是非常愚蠢的行为，这是对本身实力的不信任。
'''
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# 连接到MySQL数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db"
)
cursor = conn.cursor()

# 创建GUI窗口
root = tk.Tk()
root.title("序列号检查程序")

# 创建标签和输入框
label = tk.Label(root, text="请输入6位数字及英文序列号：")
label.pack()
entry = tk.Entry(root, width=20)
entry.pack()

def check_serial_number():
    input_serial_number = entry.get()
    if len(input_serial_number) == 6:
        cursor.execute("SELECT * FROM serial_numbers WHERE number=%s", (input_serial_number,))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("重复检查", "序列号重复，请更换！")
        else:
            try:
                cursor.execute("INSERT INTO serial_numbers (number) VALUES (%s)", (input_serial_number,))
                conn.commit()
                messagebox.showinfo("插入结果", "序列号添加成功！")
            except mysql.connector.IntegrityError:
                messagebox.showinfo("插入结果", "序列号已存在，无法重复添加！")
    else:
        messagebox.showinfo("输入错误", "输入序列号长度不符合要求！")

# 创建检查按钮
check_button = tk.Button(root, text="检查序列号", command=check_serial_number)
check_button.pack()

# 运行主循环
root.mainloop()

# 关闭数据库连接
conn.close()