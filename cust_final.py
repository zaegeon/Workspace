import pandas as pd
import os

t0 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust0.csv")
t1 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust1.csv")
t2 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust2.csv")
t3 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust3.csv")
t4 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust4.csv")
test = pd.concat([t0, t1, t2, t3, t4])

test = test[['ue_cd', 'member_no', 'mock_apply_dt']]
test = test.sort_values(by = 'mock_apply_dt')

app_date = sorted(test['mock_apply_dt'].unique()) # 모의지원 일자
# len(app_date) # 33
app_date = app_date[:-8] # 2021-12-10 ~ 2022-01-03

uni_lst = sorted(test['ue_cd'].unique())
# len(uni_lst) # 5389
os.chdir('C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/final')

dir = 'C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/final'

for day in app_date:
    moji = test[test['mock_apply_dt'] == day]  # day별 모의지원 DataFrame 생성
    df_top10 = pd.DataFrame(columns=['학과코드', '지원학과코드', '지원수'], index=None)
    for i in range(len(uni_lst)):
        members = sorted(moji[moji['ue_cd'] == uni_lst[i]]['member_no'].unique())

        a = list()
        for j in members:
            a.extend(list(moji[moji['member_no'] == j]['ue_cd']))
            df = pd.DataFrame(a).value_counts().head(11)
            df = pd.DataFrame(df)

            df['학과코드'] = uni_lst[i]
            df['지원학과코드'] = df.index
            df = df.rename(columns={0:'지원수'})

        df_top10 = pd.concat([df_top10, df], axis=0)

    df_top10.to_excel(dir + '/cust_data_' + day + '.xlsx')