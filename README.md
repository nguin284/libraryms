# LibraryMS v0.1

## Mo ta

LibraryMS la ung dung quan ly thu vien don gian duoc xay dung bang Flask.

## Chuc nang

- Hien thi danh sach sach
- Loc sach theo the loai
- Xem chi tiet sach
- API danh sach sach
- API chi tiet sach
- Xu ly loi 404 cho trang web
- Xu ly loi 404 cho API

## Cai dat

Tao moi truong ao:

python -m venv venv

Kich hoat moi truong ao tren Windows:

venv\Scripts\activate

Cai dat thu vien:

pip install -r requirements.txt

## Chay ung dung

python -m flask --app app run

Sau do truy cap:

http://127.0.0.1:5000/

## Cac route

- /
- /books
- /books/<book_id>
- /api/books
- /api/books/<book_id>

## Loc theo the loai

Vi du:

/books?category=Lap%20trinh
