import flet as ft
from diseases_data import DISEASES

# ============================================================
# دیتای مراکز بهداشتی
# ============================================================
DEFAULT_SERVICES = ["vaccination", "maternal", "counseling", "medicine"]

SERVICE_LABELS = {
    "vaccination": ("💉", "واکسیناسیون"),
    "maternal":    ("🤰", "مراقبت مادران"),
    "counseling":  ("🗣️", "مشاوره"),
    "medicine":    ("💊", "توزیع دارو"),
    "child":       ("🧒", "مراقبت کودکان"),
    "lab":         ("🧪", "آزمایشگاه"),
    "diabetes":    ("🩸", "کنترل قند خون"),
    "elderly":     ("👴", "مراقبت سالمندان"),
    "dental":      ("🦷", "دندانپزشکی"),
    "nutrition":   ("🥗", "مشاوره تغذیه"),
    "hepatitis_c": ("🧬", "درمان هپاتیت C"),
    "rabies":      ("🐕", "پیشگیری از هاری"),
}


def format_phone(phone: str) -> str:
    """تبدیل 02634574939 به 026-34574939 برای نمایش"""
    if not phone:
        return ""
    # موبایل (شروع با 09 یا 9)
    if phone.startswith("09") and len(phone) == 11:
        return f"{phone[:4]}-{phone[4:]}"
    # تلفن ثابت با کد شهر
    if phone.startswith("0") and len(phone) == 11:
        return f"{phone[:3]}-{phone[3:]}"
    # بقیه حالت‌ها رو دست‌نخورده برگردون
    return phone


CENTERS = [
    # --- حصارک / آزادگان ---
    {"id": 1, "name": "مرکز خدمات جامع سلامت آزادگان",
     "address": "حصارک پایین، خیابان فروردین، جنب آتش نشانی و پارکینگ طبقاتی",
     "phone": "02634574939", "lat": 35.8362, "lng": 50.9374,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 2, "name": "پایگاه سلامت ضمیمه آزادگان",
     "address": "حصارک پایین، خیابان فروردین، جنب آتش نشانی",
     "phone": "02634554530", "lat": 35.8362, "lng": 50.9374, "services": None},
    {"id": 3, "name": "مرکز خدمات جامع سلامت شهدای حصارک بالا",
     "address": "خیابان شهید بهشتی، سه راه سرم سازی، بلوار آزادی، نبش خیابان شهید خراسانی",
     "phone": "02634557464", "lat": 35.8360, "lng": 50.9380,
     "services": ["vaccination", "maternal", "counseling", "medicine", "rabies"]},
    {"id": 4, "name": "پایگاه سلامت ضمیمه حصارک بالا",
     "address": "خیابان شهید بهشتی، سه راه سرم سازی، بلوار آزادی",
     "phone": "02634557464", "lat": 35.8360, "lng": 50.9380, "services": None},
    {"id": 5, "name": "پایگاه سلامت شماره یک حصارک بالا",
     "address": "حصارک، خیابان آقا رضایی، ضلع جنوبی میدان کاوه، جنب باشگاه تختی",
     "phone": "02634554298", "lat": 35.8365, "lng": 50.9390, "services": None},
    {"id": 6, "name": "مرکز تشخیص و درمان هپاتیت C",
     "address": "خیابان شهید بهشتی، سه راه سرم سازی، بلوار آزادی، نبش خیابان شهید خراسانی",
     "phone": "02634557464", "lat": 35.8360, "lng": 50.9380,
     "services": ["hepatitis_c", "counseling", "lab"]},
    {"id": 7, "name": "مرکز پیشگیری از هاری",
     "address": "خیابان شهید بهشتی، سه راه سرم سازی، بلوار آزادی، نبش خیابان شهید خراسانی",
     "phone": "02634557464", "lat": 35.8360, "lng": 50.9380,
     "services": ["rabies", "vaccination"]},

    # --- مهرشهر / آق تپه ---
    {"id": 8, "name": "مرکز خدمات جامع سلامت شهدای آق تپه",
     "address": "مهرشهر، بلوار ارم، خیابان پنجم شرقی آق تپه، ابتدای خیابان ولیعصر",
     "phone": "02633309001", "lat": 35.7789, "lng": 50.8653,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 9, "name": "پایگاه سلامت ضمیمه آق تپه",
     "address": "مهرشهر، بلوار ارم، خیابان پنجم شرقی آق تپه",
     "phone": "02633309001", "lat": 35.7789, "lng": 50.8653, "services": None},
    {"id": 10, "name": "پایگاه سلامت شماره یک آق تپه",
     "address": "آق تپه، خیابان دوم غربی، انتهای خیابان، مهر ۳",
     "phone": "02633341215", "lat": 35.7795, "lng": 50.8640, "services": None},
    {"id": 11, "name": "پایگاه سلامت شماره دو آق تپه",
     "address": "آق تپه، خیابان ولیعصر، خیابان عدل ۵",
     "phone": "02633313106", "lat": 35.7800, "lng": 50.8650, "services": None},
    {"id": 12, "name": "مرکز خدمات جامع سلامت شهید مرتضی آوینی",
     "address": "مهرشهر، بلوار ارم، شهرک کیانمهر، میدان امام خمینی، نبش میدان",
     "phone": "02633204636", "lat": 35.7710, "lng": 50.8690,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 13, "name": "پایگاه سلامت ضمیمه آوینی",
     "address": "مهرشهر، کیانمهر، میدان امام خمینی",
     "phone": "02633204636", "lat": 35.7710, "lng": 50.8690, "services": None},
    {"id": 14, "name": "پایگاه سلامت شماره دو کیانمهر",
     "address": "کیانمهر، بلوار امیر کبیر، بلوار نور، بلوار چنار، کوچه باران ۱۱، درمانگاه آویژه",
     "phone": "02691090785", "lat": 35.7720, "lng": 50.8680, "services": None},
    {"id": 15, "name": "مرکز خدمات جامع سلامت شهدای مهرشهر",
     "address": "فاز ۴ مهرشهر، چهارراه هنرستان، نبش خیابان ۴۰۵ شرقی",
     "phone": "02633501886", "lat": 35.7720, "lng": 50.8720,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 16, "name": "پایگاه سلامت ضمیمه مهرشهر",
     "address": "فاز ۴ مهرشهر، چهارراه پاسگاه، بین ۴۱۱ و ۴۱۲ شرقی، پلاک ۹۰",
     "phone": "02633501257", "lat": 35.7725, "lng": 50.8725, "services": None},
    {"id": 17, "name": "پایگاه سلامت شماره یک مهرشهر",
     "address": "فاز ۴ مهرشهر، بلوار رزهبان، خ ۴۰۲ غربی، ساختمان پارسا",
     "phone": "02633523321", "lat": 35.7730, "lng": 50.8730, "services": None},
    {"id": 18, "name": "پایگاه سلامت شماره سه مهرشهر",
     "address": "مهرشهر، گلستان، نبش خیابان ششم شقایق، داخل محوطه مسجد بعثت",
     "phone": "02633400901", "lat": 35.7740, "lng": 50.8740, "services": None},
    {"id": 19, "name": "مرکز خدمات جامع سلامت شهید علی گزلی",
     "address": "حسین آباد مهرشهر، چهارراه فرهنگ، بلوار ولیعصر، جنب پل زیرگذر، خیابان طلوع پلاک ۳۰",
     "phone": "02633311024", "lat": 35.7900, "lng": 50.8850,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 20, "name": "پایگاه سلامت ضمیمه گزلی",
     "address": "حسین آباد مهرشهر، چهارراه فرهنگ، بلوار ولیعصر",
     "phone": "02633311024", "lat": 35.7900, "lng": 50.8850, "services": None},
    {"id": 21, "name": "پایگاه سلامت شماره یک گزلی",
     "address": "اخترآباد، ۱۲ متری مهستان دو، نبش فرعی هفتم",
     "phone": "09044619245", "lat": 35.7880, "lng": 50.8830, "services": None},
    {"id": 22, "name": "پایگاه سلامت شماره دو گزلی",
     "address": "حسین آباد مهرشهر، خیابان فرهنگ، کوچه شهید سیروس مهدی زاده، پلاک ۸۰",
     "phone": "02633306031", "lat": 35.7895, "lng": 50.8845, "services": None},

    # --- ماهدشت و اطراف ---
    {"id": 23, "name": "مرکز خدمات جامع سلامت آموزگار",
     "address": "ماهدشت، سردارآباد، روبروی مدرسه شهدا",
     "phone": "02637304333", "lat": 35.7285, "lng": 50.8130,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 24, "name": "پایگاه سلامت ضمیمه آموزگار",
     "address": "ماهدشت، سردارآباد، روبروی مدرسه شهدا",
     "phone": "02637304333", "lat": 35.7285, "lng": 50.8130, "services": None},
    {"id": 25, "name": "پایگاه سلامت شماره دو احمدآباد",
     "address": "ماهدشت، خیابان سردارآباد، احمدآباد",
     "phone": "02637858487", "lat": 35.7290, "lng": 50.8140, "services": None},
    {"id": 26, "name": "پایگاه سلامت شماره سه راشته",
     "address": "ماهدشت، کوی راشته",
     "phone": "02637870093", "lat": 35.7270, "lng": 50.8100, "services": None},
    {"id": 27, "name": "پایگاه سلامت ضمیمه حمزه سیدالشهدا",
     "address": "جاده ماهدشت، شهرک چمران، خیابان نور ۴۰ (لاله)",
     "phone": "02636303332", "lat": 35.7300, "lng": 50.8150, "services": None},
    {"id": 28, "name": "مرکز خدمات جامع سلامت شهدای عباس آباد",
     "address": "جاده ماهدشت، بعد از ولدآباد کوچک، عباس آباد، خیابان طالقانی",
     "phone": "02636302253", "lat": 35.7250, "lng": 50.8080,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 29, "name": "مرکز خدمات جامع سلامت شهدای قزل قشلاق",
     "address": "جاده ماهدشت، جعفرآباد، شهرک قزل قشلاق، خیابان غدیر ۱۸",
     "phone": "02636302002", "lat": 35.7320, "lng": 50.8200,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 30, "name": "مرکز خدمات جامع سلامت شهید علی گروسی",
     "address": "ماهدشت، میدان آزادگان، خیابان شهید بهشتی",
     "phone": "02637302688", "lat": 35.7260, "lng": 50.8070,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 31, "name": "پایگاه سلامت ضمیمه گروسی",
     "address": "ماهدشت، میدان آزادگان، خیابان شهید بهشتی",
     "phone": "02637302688", "lat": 35.7260, "lng": 50.8070, "services": None},
    {"id": 32, "name": "پایگاه سلامت شماره یک ماهدشت",
     "address": "ماهدشت، محله الزهرا، خیابان کارخانه قند، کوچه نیلوفر ۷، پلاک ۱۱",
     "phone": "02637301685", "lat": 35.7250, "lng": 50.8060, "services": None},

    # --- ولدآباد ---
    {"id": 33, "name": "مرکز خدمات جامع سلامت شهدای ولدآباد ۲ بزرگ",
     "address": "ولدآباد بزرگ، بلوار بسیج، جنب پارک آزادگان",
     "phone": "02636304222", "lat": 35.7500, "lng": 50.8480,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 34, "name": "پایگاه سلامت ضمیمه ولدآباد",
     "address": "ولدآباد بزرگ، بلوار بسیج، جنب پارک آزادگان",
     "phone": "02636304222", "lat": 35.7500, "lng": 50.8480, "services": None},
    {"id": 35, "name": "پایگاه روستایی علی آبادگونه",
     "address": "ولدآباد بزرگ، روستای علی آبادگونه",
     "phone": "02636332988", "lat": 35.7480, "lng": 50.8400, "services": None},
    {"id": 36, "name": "پایگاه سلامت شماره یک آل طه",
     "address": "محمدشهر، ولدآباد بزرگ، محله اصفهانیها، خیابان ابوذرغفاری، کوچه شقایق",
     "phone": "02636316856", "lat": 35.7510, "lng": 50.8460, "services": None},
    {"id": 37, "name": "خانه بهداشت گلستانک",
     "address": "روستای گلستانک",
     "phone": "02634011902", "lat": 35.8100, "lng": 50.8800, "services": None},

    # --- محمدشهر ---
    {"id": 38, "name": "مرکز خدمات جامع سلامت حضرت خدیجه (س)",
     "address": "محمدشهر، تپه قشلاق، خیابان خبرنگاران، جنب مجتمع آموزش استثنایی فاطمه الزهرا (س)",
     "phone": "02634224607", "lat": 35.7455, "lng": 50.8680,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 39, "name": "مرکز خدمات جامع سلامت سید احمد طباطبایی",
     "address": "محمدشهر، خیابان مصطفی خمینی، خیابان بختیاری",
     "phone": "02636312220", "lat": 35.7440, "lng": 50.8670,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 40, "name": "پایگاه سلامت ضمیمه طباطبایی",
     "address": "محمدشهر، خیابان مصطفی خمینی، خیابان بختیاری",
     "phone": "02636312220", "lat": 35.7440, "lng": 50.8670, "services": None},
    {"id": 41, "name": "پایگاه سلامت شماره دو محمدشهر",
     "address": "محمدشهر، شهرک طالقانی، کوچه مصیب زاده (تختی ۱۴)، پلاک ۴",
     "phone": "02636312036", "lat": 35.7450, "lng": 50.8690, "services": None},

    # --- شاهین ویلا / بنیاد ---
    {"id": 42, "name": "مرکز خدمات جامع سلامت شهید محمد حاجی زاده",
     "address": "میان جاده، بلوار باغستان، خیابان قلم، نبش خیابان ۱۸، جنب بانک ملی",
     "phone": "02634374259", "lat": 35.8280, "lng": 50.9680,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 43, "name": "پایگاه سلامت ضمیمه شاهین ویلا",
     "address": "شاهین ویلا، خیابان قلم، نبش خیابان نهم",
     "phone": "02634564540", "lat": 35.8290, "lng": 50.9670, "services": None},
    {"id": 44, "name": "پایگاه سلامت شماره دو شاهین ویلا",
     "address": "شاهین ویلا، بین انتهای خیابان دهم و یازدهم شرقی قلم",
     "phone": "02634312994", "lat": 35.8300, "lng": 50.9650, "services": None},
    {"id": 45, "name": "مرکز خدمات جامع سلامت ظفر (ضمیمه)",
     "address": "شاهین ویلا، بنیاد، خیابان ۲۲ بهمن جنوبی، جنب سالن ورزشی شهید همت",
     "phone": "02634570793", "lat": 35.8310, "lng": 50.9700,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 46, "name": "پایگاه سلامت ضمیمه ظفر",
     "address": "شاهین ویلا، بنیاد، خیابان ۲۲ بهمن جنوبی",
     "phone": "02634570793", "lat": 35.8310, "lng": 50.9700, "services": None},
    {"id": 47, "name": "پایگاه سلامت شماره یک بنیاد",
     "address": "بنیاد، ۲۲ بهمن جنوبی، پشت مسجد امام حسین، روبروی آسایشگاه سالمندان",
     "phone": "02634572630", "lat": 35.8315, "lng": 50.9690, "services": None},

    # --- باغستان / عدل ---
    {"id": 48, "name": "پایگاه سلامت شماره یک عدل",
     "address": "خیابان عدل، روبروی کوچه قرنی، نبش پاساژ طلا، طبقه پنجم",
     "phone": "02634513241", "lat": 35.8320, "lng": 50.9750, "services": None},
    {"id": 49, "name": "پایگاه سلامت شماره دو عدل",
     "address": "بلوار باغستان، پل حیدرآباد، جنب کتابفروشی دانش، پلاک ۴۰۵",
     "phone": "02634520045", "lat": 35.8300, "lng": 50.9720, "services": None},
    {"id": 50, "name": "مرکز خدمات جامع سلامت حضرت علی اصغر (ع)",
     "address": "میان جاده، بلوار باغستان، باغستان غربی، بوستان ۱۳، میدان ولیعصر، نبش بلوار شبنم",
     "phone": "02634304800", "lat": 35.8270, "lng": 50.9700,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 51, "name": "پایگاه سلامت ضمیمه علی اصغر",
     "address": "میان جاده، باغستان غربی، بوستان ۱۳",
     "phone": "02634304800", "lat": 35.8270, "lng": 50.9700, "services": None},
    {"id": 52, "name": "پایگاه سلامت شماره یک علی اصغر",
     "address": "باغستان، بوستان ۱۴، ساختمان پزشکی فرسام، طبقه دو، واحد ۵",
     "phone": "02634017504", "lat": 35.8275, "lng": 50.9710, "services": None},

    # --- گلشهر ---
    {"id": 53, "name": "پایگاه سلامت شماره دو گلزار",
     "address": "۴۵ متری گلشهر (بلوار شهید شمس)، چهارراه گلزار، جنب آشکده عبدی، پلاک ۱۵۸",
     "phone": "02633537298", "lat": 35.8320, "lng": 50.9850, "services": None},
    {"id": 54, "name": "پایگاه سلامت شماره سه گلزار",
     "address": "خیابان المهدی، کوچه دهقان شعار، پاساژ درخشان، طبقه سوم، واحد ۳",
     "phone": "02634613675", "lat": 35.8310, "lng": 50.9840, "services": None},
    {"id": 55, "name": "مرکز خدمات جامع سلامت شهدای گمنام",
     "address": "گلشهر، خیابان پونه شرقی، ساختمان احسان، طبقه ۴",
     "phone": "02634655404", "lat": 35.8340, "lng": 50.9880,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 56, "name": "پایگاه سلامت ضمیمه گمنام",
     "address": "کرج نو، بلوار حدادی، بلوار محمدی، پلاک ۱۴۱",
     "phone": "02634540421", "lat": 35.8350, "lng": 50.9890, "services": None},
    {"id": 57, "name": "پایگاه سلامت شماره دو گمنام",
     "address": "کرج نو، بلوار حدادی، بعد از مسجد سلمان فارسی",
     "phone": "02634250612", "lat": 35.8355, "lng": 50.9895, "services": None},

    # --- کمالشهر ---
    {"id": 58, "name": "پایگاه سلامت ضمیمه فجر انقلاب",
     "address": "خیابان امام خمینی، میلاد یک، پلاک ۹، طبقه همکف",
     "phone": "02634703204", "lat": 35.8700, "lng": 50.8650, "services": None},
    {"id": 59, "name": "پایگاه سلامت شماره یک فجر انقلاب",
     "address": "کمالشهر، میعاد ۲۱، درمانگاه شبانه روزی کمالشهر",
     "phone": "09027212382", "lat": 35.8690, "lng": 50.8640, "services": None},
    {"id": 60, "name": "مرکز خدمات سلامت شهدای کمالشهر",
     "address": "کمالشهر، خیابان شهید بهشتی، خیابان فجر ۱۲",
     "phone": "02634703824", "lat": 35.8690, "lng": 50.8630,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 61, "name": "پایگاه سلامت ضمیمه کمالشهر",
     "address": "کمالشهر، خیابان شهید بهشتی، خیابان فجر ۱۲",
     "phone": "02634703824", "lat": 35.8690, "lng": 50.8630, "services": None},
    {"id": 62, "name": "پایگاه سلامت شماره یک کمالشهر",
     "address": "کمالشهر، خیابان بهشت سکینه، خیابان شورا، خیابان شهید صادقپور، نبش قائم ۶",
     "phone": "02634720360", "lat": 35.8680, "lng": 50.8620, "services": None},

    # --- ولیعصر / خرمدشت ---
    {"id": 63, "name": "مرکز خدمات جامع سلامت ولیعصر",
     "address": "میدان حصارک، بعد از پل هوایی حصارک، شهرک خرمدشت، میثم ۳/۴",
     "phone": "02634811313", "lat": 35.8500, "lng": 50.9250,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
    {"id": 64, "name": "پایگاه سلامت ضمیمه ولیعصر",
     "address": "میدان حصارک، شهرک خرمدشت، میثم ۳/۴",
     "phone": "02634811313", "lat": 35.8500, "lng": 50.9250, "services": None},
    {"id": 65, "name": "پایگاه سلامت شماره یک پیشاهنگی ولیعصر",
     "address": "میدان حصارک، بعد از پل هوایی، شهرک پیشاهنگی، خیابان ولیعصر ۲",
     "phone": "02634815800", "lat": 35.8510, "lng": 50.9240, "services": None},
    {"id": 66, "name": "پایگاه سلامت شماره دو ولیعصر",
     "address": "خرمدشت، خیابان میثم ۲/۳، کوچه گلرنگ، درمانگاه شبانه روزی دی، طبقه سوم",
     "phone": "02634804232", "lat": 35.8490, "lng": 50.9260, "services": None},
    {"id": 67, "name": "پایگاه سلامت شماره سه ولیعصر",
     "address": "کمالشهر، خرمدشت، خیابان میثم، خیابان سعدی، پلاک ۲۷",
     "phone": "02634803417", "lat": 35.8680, "lng": 50.8700, "services": None},
    {"id": 68, "name": "پایگاه سلامت شماره چهار ولیعصر",
     "address": "پیشاهنگی، ۲۰ متری نورمنش، خیابان باکری، پلاک ۷۱، ساختمان پارسا، طبقه سوم",
     "phone": "02634825890", "lat": 35.8520, "lng": 50.9230, "services": None},

    # --- پیام ---
    {"id": 69, "name": "مرکز خدمات جامع سلامت شهید عبدالکریم گراوند",
     "address": "شهرک پیام، بلوار امام رضا، خیابان چمران، پایین‌تر از مسجد حضرت معصومه",
     "phone": "02634016320", "lat": 35.8450, "lng": 50.9450,
     "services": ["vaccination", "maternal", "counseling", "medicine"]},
]


def main(page: ft.Page):
    page.title = "خانه سلامت من"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    page.appbar = ft.AppBar(
        title=ft.Text("خانه سلامت من", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )

    # ===== پیام خوش‌آمدگویی =====
    def close_welcome(e):
        welcome_dialog.open = False
        page.update()

    welcome_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Row([
            ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE_700, size=40),
            ft.Text("به خانه سلامت من خوش آمدید", size=20,
                    weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
        ], alignment=ft.MainAxisAlignment.CENTER),
        content=ft.Container(
            content=ft.Column([
                ft.Text("این اپلیکیشن جهت آشنایی شما با بیماری‌ها و خدمات مراکز سلامت طراحی شده است.",
                        size=16, text_align=ft.TextAlign.CENTER),
                ft.Container(height=10),
                ft.Text("در این اپ می‌توانید اطلاعات کامل درباره علائم، پیشگیری و زمان مراجعه به مرکز بهداشت را برای هر بیماری مطالعه کنید.",
                        size=14, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_700),
                ft.Container(height=15),
                ft.Divider(),
                ft.Text("📍 مرکز بهداشت غرب کرج", size=14, weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_700, text_align=ft.TextAlign.CENTER),
                ft.Text("تهیه و تنظیم: آزاد کرمی", size=13, color=ft.Colors.GREY_700,
                        text_align=ft.TextAlign.CENTER),
                ft.Text("karamiazad1990@gmail.com", size=12, color=ft.Colors.GREY_500,
                        text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            padding=10,
            width=350
        ),
        actions=[
            ft.ElevatedButton("متوجه شدم، ورود", on_click=close_welcome,
                              bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER
    )

    page.overlay.append(welcome_dialog)
    welcome_dialog.open = True
    page.update()

    # ===== نمایش جزئیات بیماری =====
    def show_disease_details(e):
        disease_id = e.control.data
        disease = next((d for d in DISEASES if d["id"] == disease_id), None)
        if not disease:
            return

        def go_back(e):
            page.views.pop()
            page.update()

        page.views.append(
            ft.View(
                f"/detail/{disease['id']}",
                [
                    ft.AppBar(
                        title=ft.Text(disease["title"], color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.BLUE_700,
                        leading=ft.IconButton(ft.Icons.ARROW_BACK,
                                              icon_color=ft.Colors.WHITE,
                                              on_click=go_back)
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Container(
                                content=ft.Image(src=disease["image"], width=200, height=200,
                                                 fit=ft.ImageFit.CONTAIN,
                                                 error_content=ft.Icon(ft.Icons.IMAGE_NOT_SUPPORTED,
                                                                       size=100, color=ft.Colors.GREY_400)),
                                alignment=ft.alignment.center, padding=10
                            ),
                            ft.Row([
                                ft.Container(
                                    content=ft.Text(disease["category"], color=ft.Colors.WHITE, size=12),
                                    bgcolor=ft.Colors.RED_400 if disease["category"] == "واگیر" else ft.Colors.GREEN_600,
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    border_radius=15
                                )
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Container(height=10),
                            ft.Text(disease["title"], size=26, weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_900),
                            ft.Divider(height=20),
                            ft.Text("تعریف بیماری", size=20, weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREEN_700),
                            ft.Text(disease["definition"], size=15, text_align=ft.TextAlign.RIGHT),
                            ft.Divider(height=20),
                            ft.Text("علائم بالینی", size=20, weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.ORANGE_700),
                            ft.Text(disease["symptoms"], size=15, text_align=ft.TextAlign.RIGHT),
                            ft.Divider(height=20),
                            ft.Text("آمار و اطلاعات", size=20, weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.PURPLE_700),
                            ft.Text(disease["stats"], size=15, text_align=ft.TextAlign.RIGHT),
                            ft.Divider(height=20),
                            ft.Text("راه‌های پیشگیری", size=20, weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.TEAL_700),
                            ft.Text(disease["prevention"], size=15, text_align=ft.TextAlign.RIGHT),
                            ft.Divider(height=20),
                            ft.Text("چه زمانی به مرکز بهداشت مراجعه کنیم؟", size=20,
                                    weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
                            ft.Text(disease["when_to_visit"], size=15, text_align=ft.TextAlign.RIGHT),
                            ft.Container(height=40),
                        ], spacing=10),
                        padding=20
                    )
                ],
                scroll=ft.ScrollMode.AUTO
            )
        )
        page.update()

    # ===== لیست بیماری‌ها =====
    selected_category = {"value": "همه"}

    def get_diseases_view():
        cards = []
        filtered = (DISEASES if selected_category["value"] == "همه"
                    else [d for d in DISEASES if d["category"] == selected_category["value"]])
        for disease in filtered:
            cards.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            leading=ft.Icon(
                                ft.Icons.CORONAVIRUS if disease["category"] == "واگیر" else ft.Icons.FAVORITE,
                                color=ft.Colors.RED_400 if disease["category"] == "واگیر" else ft.Colors.GREEN_600,
                                size=40
                            ),
                            title=ft.Text(disease["title"], weight=ft.FontWeight.BOLD, size=16),
                            subtitle=ft.Text(disease["summary"], size=13, max_lines=2),
                            trailing=ft.Icon(ft.Icons.ARROW_FORWARD),
                            on_click=show_disease_details,
                            data=disease["id"]
                        ),
                        padding=5
                    )
                )
            )
        return ft.Column(cards, spacing=10)

    def set_category(cat):
        selected_category["value"] = cat
        content_area.controls.clear()
        content_area.controls.append(get_filter_buttons())
        content_area.controls.append(get_diseases_view())
        page.update()

    def get_filter_buttons():
        return ft.Row([
            ft.ElevatedButton("همه", on_click=lambda e: set_category("همه")),
            ft.ElevatedButton("واگیر", on_click=lambda e: set_category("واگیر"),
                              bgcolor=ft.Colors.RED_100),
            ft.ElevatedButton("غیرواگیر", on_click=lambda e: set_category("غیرواگیر"),
                              bgcolor=ft.Colors.GREEN_100),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    # ===== محتوای خانه =====
    home_content = ft.Column([
        ft.Container(
            content=ft.Image(src="assets/icon.png", width=100, height=100,
                             fit=ft.ImageFit.CONTAIN,
                             error_content=ft.Icon(ft.Icons.HOME, size=100,
                                                   color=ft.Colors.BLUE_700)),
            alignment=ft.alignment.center
        ),
        ft.Container(height=10),
        ft.Text("خانه سلامت من", size=28, weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900, text_align=ft.TextAlign.CENTER),
        ft.Container(height=10),
        ft.Text("به خانه سلامت من خوش آمدید", size=20, weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREEN_700, text_align=ft.TextAlign.CENTER),
        ft.Container(height=10),
        ft.Text("این اپلیکیشن جهت آشنایی شما با بیماری‌ها و خدمات مراکز سلامت طراحی شده است.",
                size=15, text_align=ft.TextAlign.CENTER),
        ft.Container(height=15),
        ft.Text(f"تعداد بیماری‌های موجود: {len(DISEASES)}", size=16,
                color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
        ft.Text(f"واگیر: {len([d for d in DISEASES if d['category']=='واگیر'])} | "
                f"غیرواگیر: {len([d for d in DISEASES if d['category']=='غیرواگیر'])}",
                size=14, color=ft.Colors.GREY_700, text_align=ft.TextAlign.CENTER),
        ft.Container(height=15),
        ft.Text(f"تعداد مراکز بهداشتی: {len(CENTERS)}", size=16,
                color=ft.Colors.GREEN_700, text_align=ft.TextAlign.CENTER),
        ft.Container(height=20),
        ft.Divider(),
        ft.Container(height=10),
        ft.Text("📍 مرکز بهداشت غرب کرج", size=15, weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREEN_700, text_align=ft.TextAlign.CENTER),
        ft.Text("تهیه و تنظیم: آزاد کرمی", size=13, color=ft.Colors.GREY_700,
                text_align=ft.TextAlign.CENTER),
        ft.Text("karamiazad1990@gmail.com", size=12, color=ft.Colors.GREY_500,
                text_align=ft.TextAlign.CENTER),
        ft.Container(height=30),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # ===== محتوای مراکز =====
    async def open_map_route(e):
        center = e.control.data
        url = ("https://www.google.com/maps/dir/?api=1"
               f"&destination={center['lat']},{center['lng']}&travelmode=driving")
        await page.launch_url(url)

    async def open_phone_call(e):
        center = e.control.data
        await page.launch_url(f"tel:{center['phone']}")

    def build_services_row(services):
        if not services:
            services = DEFAULT_SERVICES
        chips = []
        for key in services:
            icon, label = SERVICE_LABELS.get(key, ("🏥", key))
            chips.append(
                ft.Container(
                    content=ft.Text(f"{icon} {label}", size=12, color=ft.Colors.TEAL_900),
                    bgcolor=ft.Colors.TEAL_50,
                    padding=ft.padding.symmetric(horizontal=10, vertical=6),
                    border_radius=20,
                )
            )
        return ft.Row(chips, wrap=True, spacing=8, run_spacing=8)

    def build_center_card(center):
        display_phone = format_phone(center["phone"])
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(center["name"], weight=ft.FontWeight.BOLD, size=15, expand=True),
                        ft.IconButton(icon=ft.Icons.PHONE, icon_color=ft.Colors.GREEN_600,
                                      tooltip=f"تماس با {display_phone}",
                                      data=center,
                                      on_click=open_phone_call),
                        ft.IconButton(icon=ft.Icons.LOCATION_ON, icon_color=ft.Colors.RED_600,
                                      tooltip="مشاهده مسیر روی نقشه",
                                      data=center,
                                      on_click=open_map_route),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text(center["address"], size=13, color=ft.Colors.GREY_700),
                    ft.Text(f"📞 {display_phone}", size=13, color=ft.Colors.GREEN_700),
                    ft.Divider(height=12),
                    ft.Text("خدمات این مرکز:", size=13, weight=ft.FontWeight.BOLD,
                            color=ft.Colors.TEAL_700),
                    ft.Container(height=5),
                    build_services_row(center.get("services")),
                ], spacing=4),
                padding=12,
            )
        )

    centers_content = ft.Column(
        [
            ft.Text("آدرس مراکز بهداشتی", size=24, weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900),
            ft.Text("مرکز بهداشت غرب کرج", size=18, weight=ft.FontWeight.BOLD,
                    color=ft.Colors.GREEN_700),
            ft.Text(f"تعداد مراکز: {len(CENTERS)}", size=14, color=ft.Colors.GREY_700),
            ft.Text("📍 برای مسیریابی، 📞 برای تماس تلفنی مستقیم:", size=14),
            ft.Container(height=10),
        ]
        + [build_center_card(c) for c in CENTERS]
        + [ft.Container(height=30)],
        spacing=12,
    )

    content_area = ft.Column(expand=True)

    def on_nav_change(e):
        index = e.control.selected_index
        content_area.controls.clear()
        if index == 0:
            content_area.controls.append(home_content)
        elif index == 1:
            content_area.controls.append(get_filter_buttons())
            content_area.controls.append(get_diseases_view())
        elif index == 2:
            content_area.controls.append(centers_content)
        page.update()

    content_area.controls.append(home_content)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="خانه"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="آموزش بیماری‌ها"),
            ft.NavigationBarDestination(icon=ft.Icons.LOCATION_ON, label="آدرس مراکز"),
        ],
        on_change=on_nav_change,
        selected_index=0
    )

    page.add(content_area)


if __name__ == "__main__":
    ft.app(main)
