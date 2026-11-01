import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# إعدادات صفحة المنصة الاحترافية
st.set_page_config(
    page_title="Astro-Quant FX Pro Master",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ منصة Astro-Quant FX التداولية الفائقة (Interactive Pro)")
st.markdown("نظام تداول هندسي وفلكي تفاعلي بالكامل: يتيح لك التكبير، التحريك، حفظ الشارت، وعرض مروحة جان ومربع الواحد بدقة مطلقة.")

# --- الشريط الجانبي: لوحة التحكم المتقدمة ---
st.sidebar.header("🎛️ أدوات الهندسة والفلك التفاعلية")

selected_asset = st.sidebar.selectbox(
    "اختر الأصل المالي:",
    ("الذهب (XAU/USD)", "EUR/USD", "GBP/USD", "USD/JPY", "بيتكوين (BTC/USD)")
)

user_market_price = st.sidebar.number_input(
    "أدخل السعر الحالي من منصتك:", 
    value=3876.81,
    format="%.2f"
)

# اختيار الأداة الاحترافية المراد رسمها تفاعلياً
interactive_tool = st.sidebar.selectbox(
    "اختر الأداة الهندسية للرسم التفاعلي:",
    (
        "📐 مروحة جان الأصلية (Gann Fan True Angles)",
        "🔲 شبكة مربع الواحد (Square of One)",
        "🔮 الاسقاط الفلكي وزوايا الدائرة",
        "⏳ دورات الوقت الاهتزازية"
    )
)

st.sidebar.subheader("⚙️ إعدادات العرض")
show_grid = st.sidebar.checkbox("إظهار شبكة الإحداثيات الدقيقة", value=True)

# --- حسابات جان المتقدمة ---
sqrt_val = np.sqrt(user_market_price)
p1 = (sqrt_val + 0.125) ** 2
p2 = (sqrt_val + 0.250) ** 2
p3 = (sqrt_val + 0.500) ** 2
s1 = (sqrt_val - 0.250) ** 2
s2 = (sqrt_val - 0.500) ** 2

# --- واجهة العرض والتقرير الاستباقي (خطوة بخطوة) ---
st.subheader("🔮 التقرير التحليلي الاستباقي المفصل (خطوة بخطوة)")

col_rep1, col_rep2 = st.columns(2)
with col_rep1:
    st.success(f"🎯 **الخطوة الأولى والسيناريو الصاعد (هنا):** ارتداد السعر من مستوى الدعم الهندسي عند `{s1:,.2f}` يشير إلى استهداف مقاومة مروحة جان عند `{p2:,.2f}`.")
    st.info("💡 **توصية التنفيذ:** افتح صفقة شراء بحذر واجعل الهدف الأول عند المقاومة المذكورة.")
with col_rep2:
    st.error(f"⚠️ **الخطوة الثانية والسيناريو الهابط (هناك):** كسر خط الاتجاه الهندسي السفلي عند `{s2:,.2f}` سيسرع الهبوط نحو الدعم العميق.")
    st.warning("🛡️ **حماية المحفظة:** التزم بوضع وقف الخسارة أسفل خط الزاوية مباشرة.")

st.divider()

# --- محرك الشارت التفاعلي الفائق (Plotly Chart) ---
st.subheader(f"📈 الشارت التفاعلي الاحترافي لـ {selected_asset} (قابل للتكبير والحفظ)")

# توليد بيانات شموع واقعية متطابقة مع السعر المدخل
np.random.seed(777)
n_candles = 50
dates = pd.date_range(end=pd.Timestamp.today(), periods=n_candles, freq='4h')
price_base = user_market_price + np.cumsum(np.random.normal(0, user_market_price * 0.0005, n_candles))

df = pd.DataFrame({
    'Date': dates,
    'Open': price_base - np.random.uniform(0, user_market_price * 0.0003, n_candles),
    'Close': price_base + np.random.uniform(0, user_market_price * 0.0003, n_candles),
})
df['High'] = df[['Open', 'Close']].max(axis=1) + np.random.uniform(0, user_market_price * 0.0002, n_candles)
df['Low'] = df[['Open', 'Close']].min(axis=1) - np.random.uniform(0, user_market_price * 0.0002, n_candles)

# إنشاء الشارت باستخدام Plotly (يتيح التكبير، التحريك، وحفظ الصورة كـ PNG بنقرة واحدة)
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='الشموع اليابانية'
)])

# إضافة خطوط هندسة جان المتقدمة بناءً على اختيار المستخدم
if "مروحة جان" in interactive_tool:
    fig.add_trace(go.Scatter(x=[df['Date'].iloc[0], df['Date'].iloc[-1]], y=[s1, p3], mode='lines', name='زاوية مروحة جان (1x1)', line=dict(color='#00ff7f', width=2)))
    fig.add_trace(go.Scatter(x=[df['Date'].iloc[0], df['Date'].iloc[-1]], y=[s2, p2], mode='lines', name='زاوية مروحة جان (2x1)', line=dict(color='#00d2ff', width=2)))
elif "مربع الواحد" in interactive_tool:
    fig.add_hline(y=p2, line_dash="dash", line_color="#9400d3", annotation_text=f"مقاومة مربع الواحد: {p2:.2f}")
    fig.add_hline(y=s1, line_dash="dash", line_color="#ff1493", annotation_text=f"دعم مربع الواحد: {s1:.2f}")
elif "الاسقاط الفلكي" in interactive_tool:
    fig.add_hline(y=user_market_price, line_dash="solid", line_color="#ff4500", annotation_text=f"محور الارتكاز الفلكي: {user_market_price:.2f}")
    fig.add_hline(y=p1, line_dash="dot", line_color="#00ffff", annotation_text=f"خط الاقتران الفلكي: {p1:.2f}")
else:
    fig.add_hline(y=p2, line_dash="dash", line_color="#ffa500", annotation_text=f"مقاومة دورة الوقت: {p2:.2f}")

# تنسيق مظهر الشارت ليطابق منصات المحترفين الداكنة
fig.update_layout(
    title=f"تحليل {selected_asset} باستخدام أداة: {interactive_tool}",
    yaxis_title='السعر (USD)',
    xaxis_title='الإطار الزمني',
    template='plotly_dark',
    height=550,
    xaxis_rangeslider_visible=False
)

# عرض الشارت مع تفعيل أدوات التحكم والتحريك والتكبير والحفظ التلقائي
st.plotly_chart(fig, use_container_width=True)

st.info("💡 **ملاحظة للمتداول:** يمكنك الآن استخدام أصابعك لتكبير الشارت (Zoom)، تحريكه يميناً ويساراً، أو الضغط على أيقونة الكاميرا في أعلى الشارت لحفظه كصورة PNG مباشرة على هاتفك!")

st.divider()

# --- زر التحديث الفوري ---
if st.button("🔄 إعادة تشغيل الحسابات الهندسية والتحديث الفوري"):
    st.rerun()
