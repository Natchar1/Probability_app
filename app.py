import streamlit as st
import random
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager as fm
import streamlit as st
import random
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

# ตั้งค่าฟอนต์ภาษาไทย
font_path = "fonts/THSarabunNew.ttf"  # ระบุเส้นทางฟอนต์
try:
    thai_font = fm.FontProperties(fname=font_path)
    rcParams['font.family'] = thai_font.get_name()
except FileNotFoundError:
    # ใช้ฟอนต์สำรองหากไม่มีฟอนต์ภาษาไทย
    rcParams['font.family'] = 'DejaVu Sans'

# Sidebar สำหรับเลือกหน้าเกม
st.sidebar.title("เลือกเกม")
page = st.sidebar.radio("ไปยัง:", ["หน้าแรก","เกมโยนเหรียญ", "เกมทอยลูกเต๋า", "เกมสุ่มตัวเลข", "เกมหยิบลูกบอล","แบบประเมินสื่อ"])

# ฟังก์ชันสำหรับกราฟ
def plot_graph(labels, theoretical_values, experimental_values, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    bar_width = 0.35
    x = range(len(labels))

    # กราฟแท่งสำหรับทฤษฎี
    ax.bar(x, theoretical_values, bar_width, label="ทฤษฎี", alpha=0.7, color='steelblue')
    # กราฟแท่งสำหรับการทดลอง
    ax.bar([i + bar_width for i in x], experimental_values, bar_width, label="การทดลอง", alpha=0.7, color='orange')

    ax.set_xlabel("ผลลัพธ์", fontsize=14, fontproperties=thai_font)
    ax.set_ylabel("ความน่าจะเป็น (%)", fontsize=14, fontproperties=thai_font)
    ax.set_title(title, fontsize=16, fontproperties=thai_font)
    ax.set_xticks([i + bar_width / 2 for i in x])
    ax.set_xticklabels(labels, fontsize=12, fontproperties=thai_font)
    ax.legend(fontsize=12, loc='upper left', prop=thai_font)
    st.pyplot(fig)

if page == "หน้าแรก":
    st.title("โปรแกรมจำลองความน่าจะเป็น")
    st.image("images/Natchar.JPG", caption="", width=400)
    st.header("ผู้พัฒนา:")
    st.write("นาย นัชท์ชา ผ่องศรี" ) 
    st.write("กลุ่มสาระคณิตศาสตร์ ระดับ มัธยมศึกษาตอนปลาย")

    st.header("สื่อนี้เป็นส่วนหนึ่งของวิชา")
    st.write("คณิตศาสตร์พื้นฐาน 5 (ค33101) นักเรียนระดับชั้น ม.6")

    st.header("วัตถุประสงค์ของสื่อ:")
    st.write("""
    - เพื่อช่วยให้นักเรียนเข้าใจแนวคิดพื้นฐานของความน่าจะเป็น
    - ส่งเสริมการเรียนรู้ผ่านกิจกรรมเชิงปฏิบัติและการทดลองจริง
    - เพิ่มความสนุกและความน่าสนใจในบทเรียนวิชาคณิตศาสตร์
    """)

    st.header("รายละเอียดเกี่ยวกับสื่อ:")
    st.write("""
    โปรแกรมนี้ถูกออกแบบมาเพื่อให้นักเรียนได้เรียนรู้เกี่ยวกับความน่าจะเป็น
    ผ่านการจำลองเหตุการณ์ที่เกิดขึ้นจริง เช่น เกมโยนเหรียญ, ทอยลูกเต๋า,
    การสุ่มตัวเลข และการหยิบลูกบอลจากกล่อง
    """)

    st.header("วิธีการใช้งาน:")
    st.write("""
    1. ใช้เมนูทางด้านซ้ายเพื่อเลือกเกมหรือการจำลองที่ต้องการ
    2. ปรับค่าตัวเลือก เช่น จำนวนครั้งที่ทดลอง หรือจำนวนตัวเลขที่สุ่ม
    3. ดูผลลัพธ์จากการทดลองและเปรียบเทียบกับค่าทางทฤษฎีในรูปแบบกราฟและตัวเลข
    4. ใช้ข้อมูลที่แสดงเพื่อวิเคราะห์และสรุปผลเกี่ยวกับความน่าจะเป็น
    5. วิเคราะห์ผลที่ได้และตอบคำถามในใบงาน
    6. อภิปรายผลร่วมกันในชั้นเรียน
    """)


# หน้า 1: เกมโยนเหรียญ
elif page == "เกมโยนเหรียญ":
    st.title("เกมโยนเหรียญ")
    st.image("images/coin.png", caption="", width=300)

    num_tosses = st.slider("เลือกจำนวนครั้งที่ต้องการโยนเหรียญ", min_value=10, max_value=1000, step=10, value=100)
    
    # การทดลอง
    results = {"Head": 0, "Tail": 0}
    for _ in range(num_tosses):
        toss = random.choice(["Head", "Tail"])
        results[toss] += 1
    
    theoretical_probability = {"Head": 50, "Tail": 50}
    experimental_probability = {key: (value / num_tosses) * 100 for key, value in results.items()}
    
    # แสดงผล
    st.write(f"จำนวนการทดลอง: {num_tosses}")
    st.write(f"ผลลัพธ์การทดลอง: {results}")
    st.write(f"P(Head) = {experimental_probability['Head']:.2f}%, P(Tail) = {experimental_probability['Tail']:.2f}%")
    
    plot_graph(["Head", "Tail"], 
               [theoretical_probability["Head"], theoretical_probability["Tail"]], 
               [experimental_probability["Head"], experimental_probability["Tail"]],
               "เปรียบเทียบความน่าจะเป็นในเกมโยนเหรียญ")
    
    st.title("ใบกิจกรรมที่ 1" )
    st.write("ผลลัพธ์การทดลองวิเคราะห์ผลการโยนเหรียญ")
    st.image("images/A1.png", caption="", width=600)
    with open("activity/activity 1.pdf", "rb") as file:
        btn = st.download_button(
            label="ดาวน์โหลดใบงานเกมโยนเหรียญ",
            data=file,
            file_name="activity 1.pdf",  # ชื่อไฟล์ที่ดาวน์โหลด
            mime="application/pdf"     )

# หน้า 2: เกมทอยลูกเต๋า
elif page == "เกมทอยลูกเต๋า":
    st.title("เกมทอยลูกเต๋า")
    st.image("images/di.png", caption="", width=300)
    num_rolls = st.slider("เลือกจำนวนครั้งที่ต้องการทอยลูกเต๋า", min_value=10, max_value=1000, step=10, value=100)
    
    # การทดลอง
    results = {i: 0 for i in range(1, 7)}
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        results[roll] += 1
    
    theoretical_probability = {i: 100 / 6 for i in range(1, 7)}
    experimental_probability = {key: (value / num_rolls) * 100 for key, value in results.items()}
    
    # แสดงผล
    st.write(f"จำนวนการทดลอง: {num_rolls}")
    st.write(f"ผลลัพธ์การทดลอง: {results}")
    st.write("ความน่าจะเป็นจากการทดลอง:")
    for face, prob in experimental_probability.items():
        st.write(f"P({face}) = {prob:.2f}%")
    
    plot_graph([str(i) for i in range(1, 7)], 
               list(theoretical_probability.values()), 
               list(experimental_probability.values()),
               "เปรียบเทียบความน่าจะเป็นในเกมทอยลูกเต๋า")

    st.title("ใบกิจกรรมที่ 2" )
    st.write("การทอยลูกเต๋าและการกระจายความน่าจะเป็น")
    st.image("images/A2.png", caption="", width=600)
    with open("activity/activity 2.pdf", "rb") as file:
        btn = st.download_button(
            label="ดาวน์โหลดใบงานทอยลูกเต๋า",
            data=file,
            file_name="activity 2.pdf",  # ชื่อไฟล์ที่ดาวน์โหลด
            mime="application/pdf"     )

# หน้า 3: เกมสุ่มตัวเลข
elif page == "เกมสุ่มตัวเลข":
    st.title("เกมสุ่มตัวเลข")
    st.image("images/number.png", caption="", width=300)
    num_rolls = st.slider("เลือกจำนวนครั้งที่ต้องการสุ่มตัวเลข", min_value=10, max_value=1000, step=10, value=100)
    lower_bound = st.number_input("ช่วงตัวเลขต่ำสุด", value=1)
    upper_bound = st.number_input("ช่วงตัวเลขสูงสุด", value=10)
    
    if lower_bound >= upper_bound:
        st.error("กรุณาใส่ค่าช่วงตัวเลขที่ถูกต้อง (ต่ำสุดต้องน้อยกว่าสูงสุด)")
    else:
        # การทดลอง
        results = {i: 0 for i in range(lower_bound, upper_bound + 1)}
        for _ in range(num_rolls):
            roll = random.randint(lower_bound, upper_bound)
            results[roll] += 1
        
        theoretical_probability = {i: 100 / (upper_bound - lower_bound + 1) for i in range(lower_bound, upper_bound + 1)}
        experimental_probability = {key: (value / num_rolls) * 100 for key, value in results.items()}
        
        # แสดงผล
        st.write(f"จำนวนการทดลอง: {num_rolls}")
        st.write(f"ผลลัพธ์การทดลอง: {results}")
        st.write("ความน่าจะเป็นจากการทดลอง:")
        for num, prob in experimental_probability.items():
            st.write(f"P({num}) = {prob:.2f}%")
        
        plot_graph([str(i) for i in range(lower_bound, upper_bound + 1)], 
                   list(theoretical_probability.values()), 
                   list(experimental_probability.values()),
                   "เปรียบเทียบความน่าจะเป็นในเกมสุ่มตัวเลข")


        st.title("ใบกิจกรรมที่ 3" )
        st.write("ความน่าจะเป็นและช่วงตัวเลข")
        st.image("images/A3.png", caption="", width=600)
        with open("activity/activity 3.pdf", "rb") as file:
            btn = st.download_button(
                label="ดาวน์โหลดใบงานความน่าจะเป็นและช่วงตัวเลข",
                data=file,
                file_name="activity 3.pdf",  # ชื่อไฟล์ที่ดาวน์โหลด
                mime="application/pdf"     )

# หน้า 4: เกมหยิบลูกบอล
elif page == "เกมหยิบลูกบอล":
    # ฟังก์ชันคำนวณการจัดหมู่
    def calculate_probability(num_red, num_blue, num_draw):
        total_balls = num_red + num_blue
        theoretical_probs = {}

        # คำนวณทุกกรณีที่เป็นไปได้
        for r in range(num_draw + 1):  # จำนวนแดง (0 ถึง num_draw)
            b = num_draw - r  # จำนวนสีน้ำเงิน
            if r <= num_red and b <= num_blue:
                # ความน่าจะเป็นเชิงทฤษฎีสำหรับกรณี r แดง และ b น้ำเงิน
                p = (comb(num_red, r) * comb(num_blue, b)) / comb(total_balls, num_draw)
                theoretical_probs[f"แดง {r} : น้ำเงิน {b}"] = p * 100
        return theoretical_probs

    # ฟังก์ชันคำนวณ nCr
    def comb(n, r):
        if n < r:
            return 0
        from math import factorial
        return factorial(n) // (factorial(r) * factorial(n - r))

    # ฟังก์ชันสำหรับการทดลองสุ่มหยิบลูกบอล
    def perform_experiment(num_red, num_blue, num_draw, num_trials):
        results = Counter()

        for _ in range(num_trials):
            box = ["แดง"] * num_red + ["น้ำเงิน"] * num_blue
            draws = random.sample(box, num_draw)  # หยิบ num_draw ลูก
            red_count = draws.count("แดง")
            blue_count = draws.count("น้ำเงิน")
            results[f"แดง {red_count} : น้ำเงิน {blue_count}"] += 1

        # เปลี่ยนผลลัพธ์ให้อยู่ในรูปความน่าจะเป็น
        experimental_probs = {
            case: (count / num_trials) * 100 for case, count in results.items()
        }
        return experimental_probs

    st.title("เกมหยิบลูกบอล (การจัดหมู่)")
    st.image("images/ball.png", caption="", width=300)
    st.write("สถานการณ์: มีกล่อง 1 ใบที่มีลูกบอล 2 สี (แดงและน้ำเงิน)")

    # Input parameters
    num_red = st.number_input("จำนวนลูกบอลสีแดง", min_value=1, max_value=10, value=2)
    num_blue = st.number_input("จำนวนลูกบอลสีน้ำเงิน", min_value=1, max_value=10, value=2)
    num_draw = st.number_input("จำนวนลูกบอลที่หยิบในแต่ละครั้ง", min_value=1, max_value=20, value=3)
    num_trials = st.slider("จำนวนครั้งที่ทำการหยิบ", min_value=10, max_value=1000, step=10, value=100)

    # ตรวจสอบค่าที่เหมาะสม
    if num_draw > num_red + num_blue:
        st.error("จำนวนลูกบอลที่หยิบต้องน้อยกว่าหรือเท่ากับจำนวนลูกบอลทั้งหมดในกล่อง")
    else:
        # คำนวณความน่าจะเป็นเชิงทฤษฎี
        theoretical_probs = calculate_probability(num_red, num_blue, num_draw)

        # การทดลอง
        experimental_probs = perform_experiment(num_red, num_blue, num_draw, num_trials)

        # สร้างกราฟเปรียบเทียบ
        labels = list(theoretical_probs.keys())
        theoretical_values = [theoretical_probs[label] for label in labels]
        experimental_values = [experimental_probs.get(label, 0) for label in labels]

        fig, ax = plt.subplots(figsize=(8, 6))
        bar_width = 0.35
        x = range(len(labels))

        # กราฟแท่งสำหรับทฤษฎี
        ax.bar(x, theoretical_values, bar_width, label="ทฤษฎี", alpha=0.7, color='steelblue')
        # กราฟแท่งสำหรับการทดลอง
        ax.bar([i + bar_width for i in x], experimental_values, bar_width, label="การทดลอง", alpha=0.7, color='orange')

        ax.set_xlabel("กรณี", fontsize=14, fontproperties=thai_font)
        ax.set_ylabel("ความน่าจะเป็น (%)", fontsize=14, fontproperties=thai_font)
        ax.set_title("เปรียบเทียบความน่าจะเป็น", fontsize=16, fontproperties=thai_font)
        ax.set_xticks([i + bar_width / 2 for i in x])
        ax.set_xticklabels(labels, fontproperties=thai_font, rotation=45, fontsize=10)
        ax.legend(fontsize=12, loc='upper left', prop=thai_font)
        st.pyplot(fig)

        # แสดงผล
        st.write(f"**จำนวนลูกบอลทั้งหมด**: {num_red + num_blue} ลูก")
        st.write(f"**จำนวนลูกบอลที่หยิบในแต่ละครั้ง**: {num_draw} ลูก")
        st.write(f"**จำนวนครั้งที่ทำการทดลอง**: {num_trials} ครั้ง")

        st.write("### ผลลัพธ์จากการทดลอง:")
        for case, prob in experimental_probs.items():
            st.write(f"{case} = {prob:.2f}%")

        st.write("### ผลลัพธ์จากทฤษฎี:")
        for case, prob in theoretical_probs.items():
            st.write(f"P({case}) = {prob:.2f}%")

        st.title("ใบกิจกรรมที่ 4" )
        st.write("การจัดหมู่กับการหยิบลูกบอล")
        st.image("images/A4.png", caption="", width=600)
        with open("activity/activity 4.pdf", "rb") as file:
            btn = st.download_button(
                label="ดาวน์โหลดใบงานการจัดหมู่กับการหยิบลูกบอล",
                data=file,
                file_name="activity 4.pdf",  # ชื่อไฟล์ที่ดาวน์โหลด
                mime="application/pdf"     )
elif page == "แบบประเมินสื่อ":
    st.title("ลิงก์ประเมินสื่อ")
    st.markdown(
    """
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSeWSudzZe81WhGRZ4GKifL8OmZo6de6lY5Y4lD1adBvg9k9NQ/viewform?usp=sharing" target="_blank">
        <button style="padding:10px; font-size:16px;">ประเมินสื่อ</button>
    </a>
    """,
    unsafe_allow_html=True)
