import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้ากระดาษ
st.set_page_config(
    page_title="TGO - Thailand Greenhouse Gas Management Organization",
    page_icon="🌿",
    layout="wide"
)

# ส่วนของ CSS Custom เพื่อความสวยงาม (Tailwind ในตัว)
html_content = """
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&display=swap" rel="stylesheet">
<style>
    * { font-family: 'Kanit', sans-serif; }
    .hero-gradient { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }
    .card:hover { transform: translateY(-5px); transition: all 0.3s; }
</style>

<div class="bg-gray-50">
    <div class="hero-gradient text-white py-12 px-6 rounded-3xl mb-10 shadow-lg text-center">
        <h1 class="text-3xl md:text-5xl font-bold mb-4">อบก. (TGO)</h1>
        <p class="text-lg md:text-xl opacity-90">องค์การบริหารจัดการก๊าซเรือนกระจก (องค์การมหาชน)</p>
        <p class="text-sm mt-2 opacity-80 italic">Thailand Greenhouse Gas Management Organization (Public Organization)</p>
    </div>

    <div class="grid md:grid-cols-2 gap-8 mb-12">
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-emerald-100">
            <h2 class="text-2xl font-bold mb-4 text-emerald-800">บทบาทหน้าที่</h2>
            <p class="text-gray-600 leading-relaxed mb-4 text-lg">
                เราเป็นหน่วยงานภายใต้การกำกับดูแลของรัฐมนตรีว่าการกระทรวงทรัพยากรธรรมชาติและสิ่งแวดล้อม 
                มุ่งเน้นการให้บริการและกำหนดมาตรฐานที่เกี่ยวข้องกับการ <b>วัด การรายงาน และการทวนสอบ (MRV)</b>
            </p>
            <p class="text-gray-600 leading-relaxed text-lg">
                ให้การรับรองปริมาณการปล่อย การลด และการชดเชยก๊าซเรือนกระจก เพื่อพาประเทศไทยสู่สังคมคาร์บอนต่ำ
            </p>
        </div>
        <div class="bg-emerald-50 p-8 rounded-2xl border border-emerald-200">
            <h3 class="font-bold text-xl mb-4 text-emerald-700">จุดมุ่งหมายหลัก</h3>
            <ul class="space-y-3 text-gray-700">
                <li class="flex items-center gap-2">✅ ส่งเสริมตลาดซื้อขายก๊าซเรือนกระจก</li>
                <li class="flex items-center gap-2">✅ เป็นศูนย์กลางข้อมูลสถานการณ์ก๊าซเรือนกระจก</li>
                <li class="flex items-center gap-2">✅ พัฒนาศักยภาพหน่วยงานรัฐและเอกชน</li>
                <li class="flex items-center gap-2">✅ ให้คำแนะนำด้านการบริหารจัดการก๊าซเรือนกระจก</li>
            </ul>
        </div>
    </div>

    <div class="grid md:grid-cols-3 gap-6 text-center">
        <div class="card bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div class="text-3xl mb-2">📊</div>
            <h4 class="font-bold text-emerald-700">การรับรอง</h4>
            <p class="text-gray-500 text-sm">รับรองปริมาณการลดและชดเชยก๊าซเรือนกระจก</p>
        </div>
        <div class="card bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div class="text-3xl mb-2">🤝</div>
            <h4 class="font-bold text-emerald-700">ส่งเสริมโครงการ</h4>
            <p class="text-gray-500 text-sm">สนับสนุนการพัฒนาโครงการลดก๊าซเรือนกระจก</p>
        </div>
        <div class="card bg-white p-6 rounded-xl shadow-sm border border-gray-100">
            <div class="text-3xl mb-2">💡</div>
            <h4 class="font-bold text-emerald-700">ศูนย์ข้อมูล</h4>
            <p class="text-gray-500 text-sm">คลังความรู้และคำแนะนำด้านก๊าซเรือนกระจก</p>
        </div>
    </div>
</div>
"""

# แสดงผล HTML ใน Streamlit
components.html(html_content, height=800, scrolling=True)

# ส่วนของ Footer (ใช้ Streamlit ปกติ)
st.markdown("---")
st.caption("© 2026 TGO Thailand | ข้อมูลนี้จัดทำขึ้นเพื่อการสาธิตหน้าเว็บ")
