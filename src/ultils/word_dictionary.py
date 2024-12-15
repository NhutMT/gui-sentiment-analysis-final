# use for handle_ambiguous_words function.
sentiment_dict = {
    #Positive
    "giảm_mụn": "positive",
    "mụn_hết": "positive",
    "sạch_mụn": "positive",
    "hết_mụn": "positive",
    "đỡ_mụn": "positive",
    #Negative
    "nổi_mụn": "negative",
    "mọc_mụn": "negative",
    "mụn_mọc": "negative",
    'gây_mụn': 'negative',
     "mụn_nhiều": "negative",
    "mụn_tăng": "negative",
    "mụn_nổi": "negative"
}

# use for remove_stopword_with_protection function
protected_words = ['rất tốt','tệ','chán', 'bình_thường', 'tạm_được','khá','cũng_được','rất_tốt','tốt','10đ','100đ']  # Define the words you want to keep

# use for process_special_word function
connecting_words = ['bình_thường', 'bết_dính', 'chưa', 'chưa_đáng', 'chưa_đáng_để', 'chả',
                    'chất', 'chất_kem', 'chất_lượng', 'chẳng', 'cải', 'cải_thiện', 'da',
                    'da_dầu', 'da_dầu_mụn', 'da_khô', 'da_không_bị', 'da_lão_hóa', 'da_mặt',
                    'da_mịn', 'da_mụn', 'da_nhạy_cảm', 'dùng_chán', 'dùng_ổn', 'dị', 'dịch_vụ',
                    'giao', 'giao_hàng', 'giao_hàng_nhanh', 'giá', 'giá_cả', 'giá_rẻ', 'giá_thành',
                    'giảm', 'giảm_mụn', 'gây_mụn', 'hoàn', 'hoàn_toàn', 'hài', 'hài_lòng', 'hạn_chế',
                    'kem', 'kem_chống', 'kem_dưỡng', 'khá', 'khó', 'khó_chịu', 'không', 'không_bị',
                    'không_có', 'không_có_gì_nổi_bật', 'không_gây', 'không_hiệu', 'không_hiệu_quả',
                    'không_sạch', 'không_thấy', 'không_thực_sự', 'không_đáng', 'kém', 'làm',
                    'làm_mát', 'làm_sạch', 'mặt', 'mặt_nạ', 'mụn_ẩn', 'ngăn', 'nhờn', 'nếp',
                    'phí', 'quá', 'rít_mặt', 'rõ', 'rõ_rệt', 'rất', 'rất_thoải', 'rất_thích',
                     'rất_ưng', 'rất_ổn', 'sáng', 'sạch', 'sạch_da', 'sạch_sâu', 'sở',
                    'thoải', 'thoải_mái', 'thâm', 'thích', 'thích_lắm', 'thất', 'thất_vọng', 'trắng',
                    'tẩy', 'tẩy_sạch', 'tẩy_trang', 'tệ', 'xài', 'xài_chán', 'xài_rất', 'xài_tốt', 'đau',
                    'đáng', 'đã', 'đã_dùng', 'đạt_yêu_cầu', 'ưng_ý','đáng_tiền','cực_thích','tệ', 'bình thường',
                    'khá','cũng được','rất','tốt','giá_thành', 'giá_cả', '10đ','100đ','giảm_thâm',
                    'xịt_khoáng','thấm_nhanh','tẩy_sạch','cực_đã','rất_tốt',
                    'không_bị','mụn_li_ti','cũng_được','cũng_bình_thường','bình_thường',
                    'mùi_hương','giá_rẻ','giá_thành','giá_cả','mụn_viêm','cấp_ẩm','mờ_thâm','chân_ái',
                    'ngon', 'ngon_bổ', 'không_như', 'không_giống', 'không_hài'
                    ]