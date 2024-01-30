# Foundation Of Artificial Intelligence
    folder structure
    ├── 20120055_20120083_20120105
    │   ├── report.pdf 
    │   ├── run.sh
    │   ├── source
    │   │   ├── main.py
    │   │── input
    │   │   ├── level_1
    │   │   │   ├── input1.txt
    │   │   │   ├── input2.txt
    │   │   │   ├── input3.txt
    │   │   │   ├── input4.txt
    │   │   │   ├── input5.txt
    │   │   │── level_2
    │   │   │   ├── input1.txt
    │   │   │   ├── input2.txt
    │   │   │   ├── input3.txt
    │   │── output
    │   │   ├── level_1
    │   │   │   ├── input1
    │   │   │   │   ├── 
    │   │   │   ├── input2
    │   │   │   │   ├──
    │   │   │   ├── input3
    │   │   │   │   ├──
    │   │   │   ├── input4
    │   │   │   │   ├──
    │   │   │   ├── input5
    │   │   │── level_2
    │   │   │   ├── input1
    │   │   │   │   ├──
    │   │   │   ├── input2
    │   │   │   │   ├──
    │   │   │   ├── input3
    │   │   │   │   ├──


## report 
    report.pdf is the report of the project
    Báo cáo
    • Báo cáo cần trình bày rõ ràng, cấu trúc hợp lý. Báo cáo phải có
    thông tin các thành viên trong nhóm, phải có phần tự đánh giá
    mức độ hoàn thành đồ án theo các mức ở mục 4.1.
    • Cần giải thích và mô tả ngắn gọn cách cài đặt từng thuật toán
    mà bạn sử dụng (lưu ý không chèn code để giải thích).
    • Cần có chi phí tìm kiếm và hình minh họa (hoặc link video) ứng
    với output của từng thuật toán cho tất cả các bản đồ.
    • Trong báo cáo phải có mục tham khảo, liệt kê các tài liệu (bao
    gồm cả các link chứa code tham khảo) mà nhóm sử dụng trong
    quá trình làm đồ án.
    • Nên có phần mô tả các câu lệnh trong file run.sh 

## input files
    Về bản đồ trò chơi, sẽ có hai loại: bản đồ không có điểm thưởng và
    bản đồ có điểm thưởng. Nhiệm vụ của các bạn là cài đặt các thuật
    toán tìm kiếm và tự thiết kế các bản đồ cho hai loại trên.
        • Với trường hợp bản đồ không có điểm thưởng, các bạn sẽ cài đặt
    5 thuật toán trên để giải quyết. Các bạn sẽ tự thiết kế và báo
    cáo ít nhất 5 bản đồ tiêu biểu (các bạn nên chọn những bản đồ
    mà các thuật toán có sự khác biệt với nhau nhiều) và so sánh
    sự khác nhau giữa cách tìm đường đi trong các loại bản đồ này
    với từng chiến lược tìm kiếm khác nhau. Cụ thể với một bản đồ
    được chọn để báo cáo, các bạn sẽ nhận xét:
            – Sự khác nhau giữa các chiến lược tìm kiếm đối với bản
    đồ này được thể hiện như thế nào? (cụ thể các bạn cần
    nhận xét về tính đầy đủ, tính tối ưu, độ mở các nút, thời
    gian chạy, ... của các thuật toán). Các bạn cần vận dụng lý
    thuyết để giải thích và nên có hình vẽ hoặc video thể hiện
    quá trình tìm kiếm đường đi để minh họa.
            – Với các chiến lược tìm kiếm có thông tin, các bạn cần chọn
    nhiều hàm heuristic khác nhau và báo cáo sự khác nhau
    giữa các chiến lược đối với từng hàm heuristic.
        • Với trường hợp bản đồ có điểm thưởng, các bạn sẽ suy nghĩ cách
    giải quyết và đề xuất chiến lược để tác nhân di chuyển sao cho
    chi phí đường đi từ điểm bắt đầu đến điểm thoát khỏi mê cung
    là nhỏ nhất (lưu ý rằng tác nhân không nhất thiết phải đi qua
    hết các điểm thưởng). Các bạn cần thiết kế bản đồ với tối thiểu 3
    trường hợp: có 2, 5, 10 điểm thưởng (với các giá trị điểm thưởng
    khác nhau) trên bản đồ. Nếu các bạn không thể tìm được lời giải
    tối ưu (bất kể trong trường hợp số lượng điểm thưởng là nhiều
    hay ít), hãy đề xuất chiến lược heuristic để giải quyết, chẳng hạn
    tham lam ăn tất cả điểm thưởng theo độ lớn giá trị của chúng
    rồi mới tìm đường thoát khỏi mê cung.

        • Kích thước của các bản đồ được chọn để báo cáo phải đảm bảo
    có ít nhất một bản đồ có chiều dài lớn hơn 35 và một bản đồ có
    chiều rộng lớn hơn 15.
        • Số lượng bản đồ tối thiểu cần báo cáo và phân tích: 5 bản đồ
    đối với bản đồ không có điểm thưởng và 3 bản đồ (ứng với 3
    trường có 2, 5, 10 điểm thưởng trên bản đồ) đối với bản đồ có
    điểm thưởng.


    Mỗi kịch bản kiểm thử là một file .txt được thiết kế như sau:
    • Dòng đầu là số lượng điểm thưởng n (n = 0 với bản đồ không
    có điểm thưởng).
    • n dòng tiếp theo, mỗi dòng sẽ bao gồm 3 số nguyên x,y, z với
    x,y là tọa độ của điểm thưởng trong ma trận; z là giá trị của
    điểm thưởng, sẽ là các số nguyên âm.
    • Các dòng tiếp theo mô tả bản đồ của trò chơi. Các bạn lưu ý
    điểm kết thúc của hành trình sẽ là điểm thoát khỏi mê cung (ví
    dụ trong hình 2 thì điểm kết thúc sẽ là điểm ở dòng 2 và cột 0);
    điểm bắt đầu của tác nhân được ký hiệu bằng ký tự S; các ký
    tự x sẽ là các bức tường; các ký tự + sẽ là các điểm thưởng.

    ### Lưu ý về điểm thoát khỏi mê cung: Các bạn lưu ý bản đồ mê
    cung phải được thiết kế sao cho tồn tại duy nhất một vị trí nằm trên
    các cạnh của bản đồ để tác nhân có thể thoát ra ngoài được

    Ví dụ:
    4
    3 6 -3
    5 14 -1
    6 5 -2
    7 5 -4
    xxxxxxxxxxxxxxxxxxxxxx
    x   x   xx xx        x
          x     xxxxxxxxxx
    x x   +xx  xxxx xxx xx
    x x   x x xx   xxxx  x
    x          xx +xx  x x
    xxxxx+x x      xx  x x
    xxxxx+xxx  x x  xx   x
    x          x x Sx x  x
    xxxxx x  x x x     x x
    xxxxxxxxxxxxxxxxxxxxxx
