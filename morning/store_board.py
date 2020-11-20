def t_store_board(a, *b, **c):
    print(f"=========={a}==========")
    print()
    for m in b:
        print(m)
    print()
    for item, price in c.items():
        print(f"{item:.<20}{price:.>20}")

t_store_board("택영 Cafe", "맛있는 커피를 팝니다.", "환영해요", apple='2000', coffee='1000', bread='10000')