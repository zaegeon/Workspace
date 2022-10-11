import pandas as pd

cust0 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust0.csv")
app_date = sorted(cust0['mock_apply_dt'].unique())

dir = 'C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/arrange'

for i in app_date:
    date_dat = cust0[cust0['mock_apply_dt'] == i]
    min = date_dat.groupby('ue_cd')['mock_apply_scr'].min()
    max = date_dat.groupby('ue_cd')['mock_apply_scr'].max()
    min_cut = date_dat.groupby('ue_cd')['cut_line_scr'].min()
    max_cut = date_dat.groupby('ue_cd')['cut_line_scr'].max()
    min_pass = date_dat.groupby('ue_cd')['add_pass_scr'].min()
    max_pass = date_dat.groupby('ue_cd')['add_pass_scr'].max()
    max_com_rate = date_dat.groupby('ue_cd')['competition_apply_rate'].max()

    x = pd.concat([min, max, min_cut, max_cut, min_pass, max_pass, max_com_rate], axis=1)
    x.to_csv(dir + '/' + i + '_0.csv')

cust1 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust1.csv")
app_date = sorted(cust1['mock_apply_dt'].unique())

for i in app_date:
    date_dat = cust1[cust1['mock_apply_dt'] == i]
    min = date_dat.groupby('ue_cd')['mock_apply_scr'].min()
    max = date_dat.groupby('ue_cd')['mock_apply_scr'].max()
    min_cut = date_dat.groupby('ue_cd')['cut_line_scr'].min()
    max_cut = date_dat.groupby('ue_cd')['cut_line_scr'].max()
    min_pass = date_dat.groupby('ue_cd')['add_pass_scr'].min()
    max_pass = date_dat.groupby('ue_cd')['add_pass_scr'].max()
    max_com_rate = date_dat.groupby('ue_cd')['competition_apply_rate'].max()

    x = pd.concat([min, max, min_cut, max_cut, min_pass, max_pass, max_com_rate], axis=1)
    x.to_csv(dir + '/' + i + '_1.csv')

cust2 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust2.csv")
app_date = sorted(cust2['mock_apply_dt'].unique())

for i in app_date:
    date_dat = cust2[cust2['mock_apply_dt'] == i]
    min = date_dat.groupby('ue_cd')['mock_apply_scr'].min()
    max = date_dat.groupby('ue_cd')['mock_apply_scr'].max()
    min_cut = date_dat.groupby('ue_cd')['cut_line_scr'].min()
    max_cut = date_dat.groupby('ue_cd')['cut_line_scr'].max()
    min_pass = date_dat.groupby('ue_cd')['add_pass_scr'].min()
    max_pass = date_dat.groupby('ue_cd')['add_pass_scr'].max()
    max_com_rate = date_dat.groupby('ue_cd')['competition_apply_rate'].max()

    x = pd.concat([min, max, min_cut, max_cut, min_pass, max_pass, max_com_rate], axis=1)
    x.to_csv(dir + '/' + i + '_2.csv')

cust3 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust3.csv")
app_date = sorted(cust3['mock_apply_dt'].unique())

for i in app_date:
    date_dat = cust3[cust3['mock_apply_dt'] == i]
    min = date_dat.groupby('ue_cd')['mock_apply_scr'].min()
    max = date_dat.groupby('ue_cd')['mock_apply_scr'].max()
    min_cut = date_dat.groupby('ue_cd')['cut_line_scr'].min()
    max_cut = date_dat.groupby('ue_cd')['cut_line_scr'].max()
    min_pass = date_dat.groupby('ue_cd')['add_pass_scr'].min()
    max_pass = date_dat.groupby('ue_cd')['add_pass_scr'].max()
    max_com_rate = date_dat.groupby('ue_cd')['competition_apply_rate'].max()

    x = pd.concat([min, max, min_cut, max_cut, min_pass, max_pass, max_com_rate], axis=1)
    x.to_csv(dir + '/' + i + '_3.csv')

cust4 = pd.read_csv("C:/Users/입시플랫폼컨텐츠/Desktop/workspace/220922_로그데이터 정리/cust4.csv")
app_date = sorted(cust4['mock_apply_dt'].unique())

for i in app_date:
    date_dat = cust4[cust4['mock_apply_dt'] == i]
    min = date_dat.groupby('ue_cd')['mock_apply_scr'].min()
    max = date_dat.groupby('ue_cd')['mock_apply_scr'].max()
    min_cut = date_dat.groupby('ue_cd')['cut_line_scr'].min()
    max_cut = date_dat.groupby('ue_cd')['cut_line_scr'].max()
    min_pass = date_dat.groupby('ue_cd')['add_pass_scr'].min()
    max_pass = date_dat.groupby('ue_cd')['add_pass_scr'].max()
    max_com_rate = date_dat.groupby('ue_cd')['competition_apply_rate'].max()

    x = pd.concat([min, max, min_cut, max_cut, min_pass, max_pass, max_com_rate], axis=1)
    x.to_csv(dir + '/' + i + '_4.csv')

cust_data = pd.read_csv(dir + '/2022-01-01_3.csv', encoding='cp949')
min_scr = cust_data.groupby('학과코드')['지원자 최저점'].min()
max_scr = cust_data.groupby('학과코드')['지원자 최고점'].max()
min_cut = cust_data.groupby('학과코드')['최초합 커트라인 최저점'].min()
max_cut = cust_data.groupby('학과코드')['최초합 커트라인 최고점'].max()
min_pass = cust_data.groupby('학과코드')['최종합 커트라인 최저점'].min()
max_pass = cust_data.groupby('학과코드')['최종합 커트라인 최고점'].max()
max_com_rate = cust_data.groupby('학과코드')['당일 최종 모의지원 최고 경쟁률'].max()

x_data = pd.concat([min_scr, max_scr, min_cut, max_cut, min_pass, max_pass, max_com_rate], axis=1)
x_data.to_csv(dir + '/2022-01-01.csv')