import streamlit as st
import random
import time

# 將 LoveQuiz50 類別定義貼到這裡，或者確保它在 Streamlit 檔案中可用
# 例如，如果你已經在 Colab 中執行過原始 LoveQuiz50 類別的程式碼，
# 那麼在 Streamlit 應用中，你可能需要將其複製到此處或匯入。

class LoveQuiz50:
    def __init__(self):
        self.score = 0
        self.questions = [
            # 2016年
            {"d": "2016/09/03", "q": "Joy 抱怨火車站附近的哪家早餐店很難找？", "o": ["A. 麥當勞", "B. 摩斯漢堡", "C. 肯德基", "D. 7-11"], "a": "B", "e": "Joy 說：「買好了 摩斯真難找」。"},
            {"d": "2016/09/04", "q": "Joy 曾抱怨腳被蚊子叮成紅豆腳，當時數了幾個包？", "o": ["A. 10個", "B. 25個", "C. 30個", "D. 5個"], "a": "B", "e": "Joy 崩潰說：「25個靤，癢到不行」。"},
            {"d": "2016/09/06", "q": "Joy 說要喝飲料，阿勳霸氣回覆說要買什麼給她？", "o": ["A. 水", "B. 星巴克", "C. 更好喝的", "D. 珍珠奶茶"], "a": "C", "e": "阿勳回：「我買更好喝的給你」。"},
            {"d": "2016/09/10", "q": "阿勳曾經自誇自己是什麼？", "o": ["A. 天才", "B. 帥哥", "C. 可愛又迷人", "D. 絕世好男人"], "a": "C", "e": "阿勳說：「可愛又迷人的勳勳」。"},
            {"d": "2016/09/12", "q": "Joy 的同事看完阿勳照片後的評價是？", "o": ["A. 很高", "B. 很帥", "C. 很可愛", "D. 很老實"], "a": "B", "e": "Joy 說：「同事說很帥」。"},
            {"d": "2016/09/13", "q": "Joy 升職後，阿勳擔心的第一件事是？", "o": ["A. 會不會很累", "B. 有沒有加薪", "C. 要不要請客(被卡油)", "D. 會不會晚下班"], "a": "C", "e": "阿勳問：「啥卡油? 請客嗎」。"},
            {"d": "2016/09/14", "q": "颱風天火車停駛，主要停駛範圍是？", "o": ["A. 台北以南", "B. 嘉義以南", "C. 台中以南", "D. 全線停駛"], "a": "B", "e": "阿勳說：「嘉義以南的樣子」。"},
            {"d": "2016/09/21", "q": "阿勳飛去釜山玩，Joy 叮嚀要記得什麼？", "o": ["A. 買禮物", "B. 拍照", "C. 打電話", "D. 以上皆是"], "a": "D", "e": "Joy 說：「好好玩 旺旺禮物要記得」、「要line跟照片喔」。"},
            {"d": "2016/09/22", "q": "阿勳傳了一張星巴克照片，Joy 給他取了什麼綽號？", "o": ["A. 有錢勳", "B. 壞蛋勳", "C. 臭屁勳", "D. 咖啡勳"], "a": "C", "e": "Joy 罵說：「偷用特效 臭屁勳」。"},
            {"d": "2016/09/23", "q": "Joy 的電腦壞掉出現什麼顏色的螢幕？", "o": ["A. 紅色", "B. 藍色", "C. 黑色", "D. 白色"], "a": "B", "e": "Joy 說：「電腦壞了 藍螢幕」。"},
            {"d": "2016/09/24", "q": "阿勳去韓國參觀鯨魚博物館，看到了什麼？", "o": ["A. 活鯨魚", "B. 只有骨頭", "C. 鯊魚", "D. 企鵝"], "a": "B", "e": "阿勳說：「只有骨頭 跟小海豚」。"},
            {"d": "2016/09/26", "q": "阿勳建議 Joy 去哪裡買電腦線材？", "o": ["A. 燦坤", "B. 全國電子", "C. NOVA", "D. 光華商場"], "a": "C", "e": "阿勳建議去台中 NOVA 的欣亞。"},
            {"d": "2016/09/28", "q": "Joy 颱風天騎車出去，機車發生了什麼事？", "o": ["A. 爆胎", "B. 沒油", "C. 倒掉變髒", "D. 被偷"], "a": "C", "e": "Joy 說：「車子好髒 看起來是倒掉被牽起來了」。"},
            {"d": "2016/10/02", "q": "阿勳搭客運回新竹時，發生什麼慘劇？", "o": ["A. 坐過站", "B. 椅子壞了", "C. 冷氣壞了", "D. 旁邊人很臭"], "a": "B", "e": "阿勳說：「椅子壞了，只能躺到最底... 修不好 GG」。"},
            {"d": "2016/10/05", "q": "阿勳身體不舒服想吐，Joy 威脅要帶他去？", "o": ["A. 打針", "B. 看醫生", "C. 吃大餐", "D. 收驚"], "a": "B", "e": "Joy 說：「晚上帶你看醫生 旺旺生氣了」。"},
            {"d": "2016/10/11", "q": "Joy 弄丟了什麼東西，一直叫阿勳找？", "o": ["A. 耳環", "B. 戒指", "C. 項鍊", "D. 手錶"], "a": "C", "e": "Joy 說：「旺旺的項鍊在勳勳那」。"},
            {"d": "2016/10/14", "q": "Joy 為了手機保固，急著要找什麼？", "o": ["A. 盒子", "B. 發票/購買證明", "C. 充電器", "D. 保固卡"], "a": "B", "e": "阿勳提醒：「你要找發票給我欸 手機的 購買證明」。"},
            {"d": "2016/10/15", "q": "Joy 嘴破貼藥片，貼在哪個位置？", "o": ["A. 舌頭上", "B. 舌頭下方", "C. 臉頰內側", "D. 牙齦"], "a": "B", "e": "Joy 說：「我是舌頭下方的肉」。"},
            {"d": "2016/10/20", "q": "找宜蘭民宿時，Joy 特別指定要有什麼設備？", "o": ["A. 陽台", "B. 浴缸", "C. 早餐", "D. 腳踏車"], "a": "B", "e": "Joy 強調：「要有浴缸的喔」。"},
            {"d": "2016/10/25", "q": "Joy 在一中街吃了什麼晚餐？", "o": ["A. 雞排", "B. 滷味", "C. 蛋花湯+乾意麵", "D. 便當"], "a": "C", "e": "Joy 回報：「蛋花湯 乾意麵」。"},
            {"d": "2016/10/31", "q": "Joy 做了什麼傻事導致聊天紀錄全沒了？", "o": ["A. 摔壞手機", "B. 按到重置", "C. 刪除LINE重裝", "D. 登出帳號"], "a": "C", "e": "Joy 哀號：「把line刪了 重裝 以為訊息還在」。"},
            {"d": "2016/11/04", "q": "阿勳列出的宜蘭行程中，不包含哪一個？", "o": ["A. 金車伯朗咖啡", "B. 蘭陽博物館", "C. 台北101", "D. 柯氏蔥油餅"], "a": "C", "e": "行程包含金車、蘭陽博物館、柯氏蔥油餅等。"},
            {"d": "2016/11/07", "q": "阿勳到 Joy 家樓下時，Joy 叫阿勳做什麼？", "o": ["A. 上來", "B. 等一下", "C. 下去幫我開門", "D. 去買飲料"], "a": "C", "e": "Joy 說：「你要下去」(意思是下去接她或開門)。"},

            # 2017年
            {"d": "2017/01/29", "q": "Joy 買了一件300元的外套，阿勳的預言是？", "o": ["A. 很划算", "B. 你會後悔", "C. 很好看", "D. 幫我也買一件"], "a": "B", "e": "阿勳說：「你會後悔 以後穿外套就會記得這三百」。"},
            {"d": "2017/04/09", "q": "阿勳說面試要跟誰單挑？", "o": ["A. 總經理", "B. 美國老闆", "C. 台灣主管", "D. 人資"], "a": "B", "e": "阿勳說：「因為要先跟美國人單挑 美國老闆來面試」。"},
            {"d": "2017/05/08", "q": "Joy 早上起床哪裡痛？", "o": ["A. 頭", "B. 肚子", "C. 腳", "D. 手"], "a": "D", "e": "Joy 說：「痛痛了... 勳最愛的打」。"},
            {"d": "2017/06/29", "q": "Joy 生病想買噴喉嚨的藥，因為原本吃的藥怎樣？", "o": ["A. 沒效", "B. 太貴", "C. 太苦", "D. 太大顆"], "a": "C", "e": "Joy 說：「噴廣東好苦」。"},
            {"d": "2017/08/25", "q": "Joy 週末在家組裝什麼家具？", "o": ["A. 電腦桌", "B. 衣櫥/櫃子", "C. 鞋櫃", "D. 床架"], "a": "B", "e": "Joy 提到：「57*90衣櫥」和「3層櫃」。"},
            {"d": "2017/08/26", "q": "Joy 傳了影片給阿勳，是有關於什麼賽事？", "o": ["A. 奧運", "B. 世大運", "C. 亞運", "D. 世界盃"], "a": "B", "e": "Joy 提到鏈球員參加「世大運」。"},
            {"d": "2017/12/28", "q": "Joy 覺得被阿勳騙了，是關於什麼事？", "o": ["A. 吃飯", "B. 休假天數", "C. 禮物", "D. 獎金"], "a": "B", "e": "Joy 覺得休假沒意義：「我怎覺得被你騙了呀... 勳還是星期日就離旺去新竹了」。"},

            # 2018年
            {"d": "2018/01/10", "q": "阿勳電腦出問題，顯示什麼異常？", "o": ["A. 沒網路", "B. 中毒", "C. 高CPU使用率", "D. 螢幕黑掉"], "a": "C", "e": "阿勳說：「出來顯示高CPU」。"},
            {"d": "2018/02/09", "q": "Joy 拿到廠商送的什麼東西問阿勳要不要？", "o": ["A. 洗髮精", "B. 沐浴乳", "C. 洗面乳", "D. 護手霜"], "a": "A", "e": "Joy 問：「DR. FORMULA 抗屑洗髮精 要嗎？」。"},
            {"d": "2018/02/15", "q": "阿勳看到 Joy 煎蘿蔔糕的照片，問白白的是什麼？", "o": ["A. 蘿蔔", "B. 蛋", "C. 盤子", "D. 尚未煎的蘿蔔糕"], "a": "D", "e": "Joy 回答：「還沒煎的蘿蔔糕」。"},
            {"d": "2018/06/17", "q": "Joy 提議去桃園哪裡玩？", "o": ["A. 虎頭山", "B. 慈湖", "C. 大溪老街", "D. 拉拉山"], "a": "A", "e": "Joy 提議：「桃園 虎頭山」。"},
            {"d": "2018/08/03", "q": "Joy 大掃除掃到哪裡起水泡？", "o": ["A. 手掌", "B. 腳底", "C. 兩隻拇指", "D. 食指"], "a": "C", "e": "Joy 說：「掃到2隻拇指痛 感覺快起水泡了」。"},
            {"d": "2018/08/22", "q": "阿勳傳了照片，是在哪裡？", "o": ["A. 溫泉", "B. 冷泉", "C. 海邊", "D. 泳池"], "a": "B", "e": "Joy 回覆：「冷泉」。"},
            {"d": "2018/10/15", "q": "Joy 叫阿勳把什麼東西丟掉？", "o": ["A. 餅乾", "B. 肉鬆", "C. 糖果", "D. 麵包"], "a": "B", "e": "Joy 說：「肉鬆丟掉」。"},
            {"d": "2018/12/22", "q": "Joy 幫寶寶買了什麼？", "o": ["A. 奶粉", "B. 尿布", "C. 洗衣袋和退熱貼", "D. 玩具"], "a": "C", "e": "Joy 說：「只買洗衣袋。2歲前退熱貼」。"},

            # 2019-2020年
            {"d": "2019/07/11", "q": "阿勳去哪家戲院看電影？", "o": ["A. 威秀", "B. 日新", "C. 國賓", "D. 秀泰"], "a": "B", "e": "阿勳說：「繼續看日新」。"},
            {"d": "2019/09/25", "q": "Joy 問阿勳傳的貼圖是什麼牌子？", "o": ["A. 潮牌", "B. 名牌", "C. 路邊攤", "D. 雜牌"], "a": "A", "e": "Joy 問：「什麼潮牌」。"},
            {"d": "2019/10/28", "q": "阿勳做了一個測驗，火場生存指數幾分？", "o": ["A. 100分", "B. 80分", "C. 67分", "D. 50分"], "a": "C", "e": "阿勳說：「你的火場生存指數為67分」。"},
            {"d": "2019/10/29", "q": "Joy 做 TABATA 運動，結果哪裡抽筋？", "o": ["A. 手", "B. 腳/屁股", "C. 脖子", "D. 肚子"], "a": "B", "e": "Joy 說：「腳會抽筋耶... 看起來屁股也會抽經」。"},
            {"d": "2020/01/01", "q": "跨年時，兩人互相傳了什麼？", "o": ["A. 長篇大論", "B. 影片/貼圖", "C. 語音", "D. 紅包"], "a": "B", "e": "紀錄顯示傳送了 [影片] 和 [貼圖]。"},
            {"d": "2020/01/20", "q": "Joy 幫阿勳換了多少新鈔？", "o": ["A. 1萬", "B. 2萬", "C. 3萬", "D. 5萬"], "a": "C", "e": "Joy 說：「我先換3萬起來唷」。"},
            {"d": "2020/04/26", "q": "看到阿勳睡覺的照片，阿勳開玩笑說他睡了多久？", "o": ["A. 3小時", "B. 3天", "C. 3年", "D. 30年"], "a": "C", "e": "阿勳回：「三年前就在睡了」。"},
            {"d": "2020/08/05", "q": "阿勳說「寶寶流血了」是指哪裡流血？", "o": ["A. 手指", "B. 腳趾", "C. 牙齦", "D. 鼻子"], "a": "C", "e": "接續話題是看牙醫，Joy 回：「見紅了」。"},
            {"d": "2020/12/21", "q": "Joy 為了上課做的 PPT 只做了幾頁？", "o": ["A. 7頁", "B. 10頁", "C. 20頁", "D. 50頁"], "a": "A", "e": "Joy 說：「上課PPT才作7頁」。"},
            {"d": "2020/10/28", "q": "Joy 抱怨最近工作狀況如何？", "o": ["A. 很閒", "B. 天天加班", "C. 老闆很兇", "D. 同事很雷"], "a": "B", "e": "Joy 說：「累 今天又加班了」。"},
            {"d": "2016/09/22", "q": "Joy 給阿勳取過很多綽號，下列哪個**不是**？", "o": ["A. 臭屁勳", "B. 勳阿寶", "C. 壞蛋", "D. 帥氣勳"], "a": "D", "e": "紀錄中常出現「臭屁勳」、「勳阿寶」、「壞蛋」，Joy 雖然誇過帥，但沒當綽號叫。"},
            {"d": "2016/10/02", "q": "阿勳搭車椅子壞了，他被迫呈現什麼姿勢？", "o": ["A. 站著", "B. 躺到最底", "C. 縮成一團", "D. 趴著"], "a": "B", "e": "阿勳說：「只能躺到最底」。"}
        ]

def run_quiz():
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.questions = LoveQuiz50().questions
        random.shuffle(st.session_state.questions)
        st.session_state.answered = False
        st.session_state.feedback = ""

    st.title("💑 阿勳 & Joy 的 50 道回憶大考驗 💑")
    st.write("--- ")

    if not st.session_state.quiz_started:
        st.write("規則：點擊選項來回答問題。")
        if st.button("點此開始測驗！"):
            st.session_state.quiz_started = True
            st.experimental_rerun()
    else:
        if st.session_state.current_question_index < len(st.session_state.questions):
            q_index = st.session_state.current_question_index
            current_q = st.session_state.questions[q_index]

            st.subheader(f"第 {q_index + 1} 題 (📅 {current_q['d']}):")
            st.write(current_q['q'])

            # Display feedback if already answered
            if st.session_state.answered:
                st.markdown(st.session_state.feedback)
                if st.button("下一題"):
                    st.session_state.current_question_index += 1
                    st.session_state.answered = False
                    st.session_state.feedback = ""
                    st.experimental_rerun()
            else:
                # Display options as radio buttons
                selected_option = st.radio(
                    "請選擇你的答案：",
                    current_q['o'],
                    key=f"question_{q_index}"
                )

                if st.button("提交答案"):
                    user_ans_char = selected_option[0] # Get 'A', 'B', 'C', or 'D'
                    if user_ans_char == current_q['a']:
                        st.session_state.score += 2
                        st.session_state.feedback = "<p style='color:green;font-weight:bold;'>✅ 答對了！太厲害了！</p>"
                    else:
                        st.session_state.feedback = (
                            f"<p style='color:red;font-weight:bold;'>❌ 答錯囉...</p>" +
                            f"<p>💡 正確答案是: {current_q['a']}</p>" +
                            f"<p>📝 回憶小貼士: {current_q['e']}</p>"
                        )
                    st.session_state.answered = True
                    st.experimental_rerun()
        else:
            # Quiz finished
            st.header("測驗結束！")
            st.write("--- ")
            final_score = st.session_state.score
            st.subheader(f"🏆 最終得分: {final_score} / 100 分")

            if final_score == 100:
                st.balloons()
                st.markdown("<p style='font-size:20px; color:pink; font-weight:bold;'>💖 評語：你是 Joy 的完美伴侶！這些回憶你都刻在心裡了！</p>", unsafe_allow_html=True)
            elif final_score >= 80:
                st.markdown("<p style='font-size:20px; color:purple; font-weight:bold;'>🥰 評語：很棒喔！大部分的重要時刻你都記得清清楚楚。</p>", unsafe_allow_html=True)
            elif final_score >= 60:
                st.markdown("<p style='font-size:20px; color:orange; font-weight:bold;'>🤔 評語：及格了，但有些小細節模糊囉，該去複習聊天紀錄了！</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='font-size:20px; color:red; font-weight:bold;'>😡 評語：不及格！Joy 要森七七了，今晚請客賠罪！</p>", unsafe_allow_html=True)

            if st.button("重新開始測驗"):
                st.session_state.quiz_started = False
                st.session_state.current_question_index = 0
                st.session_state.score = 0
                st.session_state.questions = LoveQuiz50().questions # Reset questions and re-shuffle
                random.shuffle(st.session_state.questions)
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.experimental_rerun()

run_quiz()