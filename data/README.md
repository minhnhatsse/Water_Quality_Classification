## Water Quality
#### **Giới thiệu** :
- Trong bất cứ thời kỳ nào, sức khỏe của con người vẫn luôn là yếu tố hàng đầu cần được chú trọng. Trong đó nguồn nước uống là nhu cầu thiết yếu của con người và cần được sự bảo vệ của nhà nước. Việc đảm bảo vệ sinh môi trường, nguồn nước sạch mang lại lợi ích vô cùng to lớn cho nền kinh tế, giảm ảnh hưởng xấu đến sức khỏe và giảm chi phí chăm sóc sức khỏe. 

#### **Mô tả** : 
- Tệp **water_potability.csv** chứa số liệu chất lượng nước cho 3276 vùng nước khác nhau. Tập dữ liệu gồm 10 cột, trong đó 9 cột đầu là độ đo chất lượng nước và cột phân loại nước **Potability** là biến mà ta cần dự đoán.

#### **Chi tiết thuộc tính** :
- **pH value** : PH là một thông số quan trọng trong việc đánh giá cân bằng axit-bazơ của nước. Nó cũng là chỉ số về tình trạng axit hoặc kiềm của trạng thái nước. WHO đã khuyến cáo giới hạn tối đa cho phép của pH từ 6,5 đến 8,5. Phạm vi điều tra hiện tại là 6,52–6,83 nằm trong phạm vi tiêu chuẩn của WHO.

- **Hardness** : Độ cứng chủ yếu do muối canxi và magie gây nên. Những muối này được hòa tan từ các trầm tích địa chất mà qua đó nước di chuyển. Khoảng thời gian nước tiếp xúc với vật liệu tạo độ cứng giúp xác định độ cứng có trong nước thô. Độ cứng ban đầu được định nghĩa là khả năng kết tủa xà phòng của nước do Canxi và Magie gây ra.

- **Solids (Total dissolved solids - TDS)** : Nước có khả năng hòa tan nhiều loại khoáng chất vô cơ và hữu cơ hoặc muối chẳng hạn như kali, canxi, natri, bicacbonat, clorua, magiê, sunfat, v.v. Những khoáng chất này tạo ra mùi vị không mong muốn và màu loãng trong nước. Đây là thông số quan trọng cho việc sử dụng nước. Nước có giá trị TDS cao chứng tỏ nước có nhiều khoáng chất. Giới hạn mong muốn cho TDS là 500 mg/l và giới hạn tối đa là 1000 mg/l được quy định cho mục đích uống.

- **Chloramines** : Clo và chloramine là những chất khử trùng chính được sử dụng trong hệ thống nước công cộng. Chloramine thường được hình thành khi thêm amoniac vào clo để xử lý nước uống. Nồng độ clo lên tới 4 miligam trên lít (mg/L hoặc 4 phần triệu (ppm)) được coi là an toàn trong nước uống.

- **Sulfate** : Sulfate là những chất tự nhiên được tìm thấy trong khoáng chất, đất và đá. Chúng hiện diện trong không khí xung quanh, nước ngầm, thực vật và thực phẩm. Việc sử dụng thương mại chính của sulfat là trong ngành hóa chất. Nồng độ sunfat trong nước biển là khoảng 2.700 miligam trên lít (mg/L). Nó nằm trong khoảng từ 3 đến 30 mg/L ở hầu hết các nguồn cung cấp nước ngọt, mặc dù nồng độ cao hơn nhiều (1000 mg/L) được tìm thấy ở một số vị trí địa lý.

-  **Conductivity** : Nước tinh khiết không phải là chất dẫn điện tốt mà là chất cách điện tốt. Tăng nồng độ ion giúp tăng cường tính dẫn điện của nước. Nói chung, lượng chất rắn hòa tan trong nước quyết định độ dẫn điện. Độ dẫn điện (EC) thực sự đo lường quá trình ion của một dung dịch cho phép nó truyền dòng điện. Theo tiêu chuẩn của WHO, giá trị EC không được vượt quá 400 μS/cm.

- **Organic_carbon** : Tổng lượng Carbon hữu cơ (TOC) trong nguồn nước đến từ các chất hữu cơ tự nhiên đang phân hủy (NOM) cũng như các nguồn tổng hợp. TOC là thước đo tổng lượng carbon trong các hợp chất hữu cơ trong nước tinh khiết. Theo US EPA < 2 mg/L as TOC trong nước đã qua xử lý/nước uống, và < 4 mg/Lít trong nước nguồn được sử dụng để xử lý.

- **Trihalomethanes** : THMs là hóa chất có thể được tìm thấy trong nước được xử lý bằng clo. Nồng độ THMs trong nước uống thay đổi tùy theo mức độ chất hữu cơ trong nước, lượng clo cần thiết để xử lý nước và nhiệt độ của nước đang được xử lý. Mức THM lên đến 80 ppm được coi là an toàn trong nước uống.

- **Turbidity** : Độ đục của nước phụ thuộc vào lượng chất rắn tồn tại ở trạng thái lơ lửng. Nó là thước đo các đặc tính phát sáng của nước và phép thử được sử dụng để chỉ ra chất lượng xả thải đối với chất keo. Giá trị độ đục trung bình thu được đối với Wondo Genet Campus (0,98 NTU) thấp hơn giá trị khuyến nghị của WHO là 5,00 NTU.

- **Potability** : Cho biết nước có an toàn cho người tiêu dùng hay không trong đó 1 nghĩa là Uống được và 0 nghĩa là Không uống được.

#### **Nguồn tham khảo** :
- **Water Quality** : https://www.kaggle.com/datasets/adityakadiwal/water-potability
