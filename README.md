# Python_Check_Error
Nội dung kiểm tra: data ngân hàng về giao dịch của khách.  Định nghĩa: - cột ngày tháng: (khi 90% giá trị của cột có định dạng là ngày tháng) và tìm bất thường trong cột - cột số: (khi 90% giá trị của cột có định dạng là số) và tìm bất thường trong cột - cột email: (khi 90% giá trị của cột có định dạng là email) và tìm bất thường trong cột  Nếu cột có giá trị lộn xộn thì coi như là cột text  Ký tự trống không tính là giá trị
Yêu cầu đầu ra:
In ra vị trí lỗi thôi
cột 1: mấy lỗi, với mỗi lỗi thì ở hàng nào, giá trị là gì
cột 2: mấy lỗi, với mỗi lỗi thì ở hàng nào, giá trị là gì
Lưu ý:
vì mình ko biết cột nào là cột email, cột nào cột ngày tháng, ...
nên khi check thì check toàn bộ data nha ko phải chỉ 1 cột nào đó thôi

Dữ liệu trong csv:
No1,No2,No3,No4
abc123@example.org,10/15/2012,1000000,abc123@example.org
abc124@example.org,10/16/2012,1000000,abc126@france.fr
abc125@example.org,10/17/2012,,abc130@example.com
abc126@france.fr,10/18/2012,1000000,
abc127@france.fr,10/19/2012,1000000,abc140@gmail.com
abc128@france.fr,10/15/2012,1000000,10/15/2012
abc129@france.fr,10/16/2012,2000000,
abc130@example.com,10/17/2012,,10/16/2012
abc131@,,2000000,10/15/2012
abc132@example.com,10/19/2012,2000000,
,10/20/2012,2000000,abc145@en-japan.com
abc134@example.com,,,15-Oct-12
abc135@test.com,10/22/2012,3000000,18-Oct-2012
abc136@test.com,15-Oct-12,3000000,123bsdf
abc137@test.com,18-Oct-2012,3000000,2
abc138@test.com,,3000000,123bdcxv
abc139@test.com,18-Oct-2012,3000000,22-Oct-12
abc140@gmail.com,19-Oct-12,abc111,abc135@test.com
abc141@gmail.com,20-Oct-12,4000000,18-Oct-2012
32t4rt,21-Oct-12,4000000,
abc143@gmail.com,22-Oct-12,4000000,18-Oct-2012
abc144@gmail.com,15-Oct-12,4000000,1
abc145@en-japan.com,18-Oct-2012,4000000,4325vb
abc146@en-japan.com,17-Oct-12,4000000,324cvbcv
abc147@en-japan.com,18-Oct-2012,4000000,2
abc148@en-japan.com,19-Oct-12,4000000,17-Oct-12
abc149@business.com,345vbcx,4000000,4
abc150@business.com,20-Oct-12,4000000,3467cvbdcb
abc151@business.com,21-Oct-12,29000000,235cvb
abc152@business.com,22-Oct-12,30000000,4
