print("<<<<<<<<<BANK DENOMINATION>>>>>>>>")


money = 13243

print("PH Bank denomination")
print("money deposit-------->",money)

dot = money // 1000
dot_exchange = money % 1000

dof = dot_exchange // 500
dof_exchange = dot_exchange % 500

dtw = dof_exchange // 200
dtw_exchange = dof_exchange % 200 

don = dtw_exchange // 100
don_exchange = dtw_exchange % 100 

dfv = don_exchange // 50
dfv_exchange = don_exchange % 50

dtt = dfv_exchange // 20
dtt_exchange = dfv_exchange % 20 

dtn = dtt_exchange // 10
dtn_exchange = dtt_exchange % 10 

df = dtn_exchange // 5
df_exchange = dtn_exchange % 5 

done = df_exchange // 1
done_exchange = df_exchange % 1 

print()
print("\n1000 -",dot)
print("\n 500 -",dof)
print("\n 200 -",dtw)
print("\n 100 -",don)
print("\n  50 -",dfv)
print("\n  20 -",dtt)
print("\n  10 -",dtn)
print("\n   5 -",df)
print("\n   1 -",done)