import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]    
# })

# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0))

# st.table(df)

# """
# # 章
# ## えらい

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['A', 'B', 'C']
# )

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

st.title('Streamlit 超入門')

st.write('Image')

# if st.checkbox('Show Image'):

#     img = Image.open('sketch1544364953196.jpg')
#     st.image(img, caption='sample', use_container_width =True)


# option = st.selectbox(
#     'あなたの好きな数字を教えてください',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は、', option, 'です。'

st.write('Interactiove widgets')

test = st.sidebar.text_input(
    'あなたの趣味を教えてください'
)

'あなたの趣味', test


# ツーアウトレイアウト

left_column, right_column = st.columns(2)
botton = left_column.button('右カラムに文字を表示')
if botton:
    right_column.write('ここは右カラムです。')

col1, col2 = st.columns(2)

# 左側のカラムに内容を表示
with col1:
    st.header("左側のカラム")
    st.write("ここは左側です。")

# 右側のカラムに内容を表示
with col2:
    st.header("右側のカラム")
    st.write("ここは右側です。")

