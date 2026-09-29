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
}

CENTERS = [
    {
        "id": 1,
        "name": "مرکز بهداشت شماره ۱",
        "address": "خیابان اصلی، پلاک ۱۰",
        "phone": "0211234567",
        "lat": 35.8320,
        "lng": 50.9915,
        "services": ["vaccination", "maternal", "counseling", "medicine"],
    },
    {
        "id": 2,
        "name": "مرکز بهداشت شماره ۲",
        "address": "میدان انقلاب، جنب بیمارستان",
        "phone": "0217654321",
        "lat": 35.8405,
        "lng": 50.9392,
        "services": ["child", "lab", "diabetes"],
    },
    {
        "id": 3,
        "name": "مرکز بهداشت شماره ۳",
        "address": "خیابان شهید بهشتی، کوچه گلستان",
        "phone": "0219876543",
        "lat": 35.8180,
        "lng": 50.9550,
        "services": None,
    },
]


def main(page: ft.Page):
    page.title = "خانه سلامت من"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    page.appbar = ft.AppBar(
        title=ft.Text("خانه سلامت من", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True,
    )

    # ===== پیام خوش‌آمدگویی =====
    def close_welcome(e):
        welcome_dialog.open = False
        page.update()

    welcome_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            [
                ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE_700, size=40),
                ft.Text(
                    "به خانه سلامت من خوش آمدید",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_900,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "این اپلیکیشن جهت آشنایی شما با بیماری‌ها و خدمات مراکز سلامت طراحی شده است.",
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        "در این اپ می‌توانید اطلاعات کامل درباره علائم، پیشگیری و زمان مراجعه به مرکز بهداشت را برای هر بیماری مطالعه کنید.",
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.GREY_700,
                    ),
                    ft.Container(height=15),
                    ft.Divider(),
                    ft.Text(
                        "📍 مرکز بهداشت غرب کرج",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_700,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "تهیه و تنظیم: آزاد کرمی",
                        size=13,
                        color=ft.Colors.GREY_700,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "karamiazad1990@gmail.com",
                        size=12,
                        color=ft.Colors.GREY_500,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
            padding=10,
            width=350,
        ),
        actions=[
            ft.Button(
                content=ft.Text("متوجه شدم، ورود"),
                on_click=close_welcome,
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
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
                        leading=ft.IconButton(
                            ft.Icons.ARROW_BACK,
                            icon_color=ft.Colors.WHITE,
                            on_click=go_back,
                        ),
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Image(
                                        src=disease["image"],
                                        width=200,
                                        height=200,
                                        fit=ft.ImageFit.CONTAIN,
                                        error_content=ft.Icon(
                                            ft.Icons.IMAGE_NOT_SUPPORTED,
                                            size=100,
                                            color=ft.Colors.GREY_400,
                                        ),
                                    ),
                                    alignment=ft.Alignment.CENTER,
                                    padding=10,
                                ),
                                ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Text(
                                                disease["category"],
                                                color=ft.Colors.WHITE,
                                                size=12,
                                            ),
                                            bgcolor=ft.Colors.RED_400
                                            if disease["category"] == "واگیر"
                                            else ft.Colors.GREEN_600,
                                            padding=ft.Padding(horizontal=10, vertical=5),
                                            border_radius=15,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Container(height=10),
                                ft.Text(
                                    disease["title"],
                                    size=26,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_900,
                                ),
                                ft.Divider(height=20),
                                ft.Text(
                                    "تعریف بیماری",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREEN_700,
                                ),
                                ft.Text(
                                    disease["definition"],
                                    size=15,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Divider(height=20),
                                ft.Text(
                                    "علائم بالینی",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.ORANGE_700,
                                ),
                                ft.Text(
                                    disease["symptoms"],
                                    size=15,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Divider(height=20),
                                ft.Text(
                                    "آمار و اطلاعات",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.PURPLE_700,
                                ),
                                ft.Text(
                                    disease["stats"],
                                    size=15,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Divider(height=20),
                                ft.Text(
                                    "راه‌های پیشگیری",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.TEAL_700,
                                ),
                                ft.Text(
                                    disease["prevention"],
                                    size=15,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Divider(height=20),
                                ft.Text(
                                    "چه زمانی به مرکز بهداشت مراجعه کنیم؟",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.RED_700,
                                ),
                                ft.Text(
                                    disease["when_to_visit"],
                                    size=15,
                                    text_align=ft.TextAlign.RIGHT,
                                ),
                                ft.Container(height=40),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            )
        )
        page.update()

    # ===== لیست بیماری‌ها =====
    selected_category = {"value": "همه"}

    def get_diseases_view():
        cards = []
        filtered = (
            DISEASES
            if selected_category["value"] == "همه"
            else [d for d in DISEASES if d["category"] == selected_category["value"]]
        )
        for disease in filtered:
            cards.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            leading=ft.Icon(
                                ft.Icons.CORONAVIRUS
                                if disease["category"] == "واگیر"
                                else ft.Icons.FAVORITE,
                                color=ft.Colors.RED_400
                                if disease["category"] == "واگیر"
                                else ft.Colors.GREEN_600,
                                size=40,
                            ),
                            title=ft.Text(
                                disease["title"],
                                weight=ft.FontWeight.BOLD,
                                size=16,
                            ),
                            subtitle=ft.Text(disease["summary"], size=13, max_lines=2),
                            trailing=ft.Icon(ft.Icons.ARROW_FORWARD),
                            on_click=show_disease_details,
                            data=disease["id"],
                        ),
                        padding=5,
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
        return ft.Row(
            [
                ft.Button(content=ft.Text("همه"), on_click=lambda e: set_category("همه")),
                ft.Button(
                    content=ft.Text("واگیر"),
                    on_click=lambda e: set_category("واگیر"),
                    bgcolor=ft.Colors.RED_100,
                ),
                ft.Button(
                    content=ft.Text("غیرواگیر"),
                    on_click=lambda e: set_category("غیرواگیر"),
                    bgcolor=ft.Colors.GREEN_100,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

    # ===== محتوای خانه =====
    home_content = ft.Column(
        [
            ft.Container(
                content=ft.Image(
                    src="assets/icon.png",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                    error_content=ft.Icon(
                        ft.Icons.HOME, size=100, color=ft.Colors.BLUE_700
                    ),
                ),
                alignment=ft.Alignment.CENTER,
            ),
            ft.Container(height=10),
            ft.Text(
                "خانه سلامت من",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=10),
            ft.Text(
                "به خانه سلامت من خوش آمدید",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREEN_700,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=10),
            ft.Text(
                "این اپلیکیشن جهت آشنایی شما با بیماری‌ها و خدمات مراکز سلامت طراحی شده است.",
                size=15,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=15),
            ft.Text(
                f"تعداد بیماری‌های موجود: {len(DISEASES)}",
                size=16,
                color=ft.Colors.BLUE_700,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Text(
                f"واگیر: {len([d for d in DISEASES if d['category']=='واگیر'])} | "
                f"غیرواگیر: {len([d for d in DISEASES if d['category']=='غیرواگیر'])}",
                size=14,
                color=ft.Colors.GREY_700,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=20),
            ft.Divider(),
            ft.Container(height=10),
            ft.Text(
                "📍 مرکز بهداشت غرب کرج",
                size=15,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREEN_700,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Text(
                "تهیه و تنظیم: آزاد کرمی",
                size=13,
                color=ft.Colors.GREY_700,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Text(
                "karamiazad1990@gmail.com",
                size=12,
                color=ft.Colors.GREY_500,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=30),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # ===== محتوای مراکز =====
    def open_map_route(e):
        center = e.control.data
        url = (
            "https://www.google.com/maps/dir/?api=1"
            f"&destination={center['lat']},{center['lng']}&travelmode=driving"
        )
        page.launch_url(url)

    def open_phone_call(e):
        center = e.control.data
        page.launch_url(f"tel:{center['phone']}")

    def build_services_row(services):
        if not services:
            services = DEFAULT_SERVICES
        chips = []
        for key in services:
            icon, label = SERVICE_LABELS.get(key, ("🏥", key))
            chips.append(
                ft.Container(
                    content=ft.Text(
                        f"{icon} {label}", size=12, color=ft.Colors.TEAL_900
                    ),
                    bgcolor=ft.Colors.TEAL_50,
                    padding=ft.Padding(horizontal=10, vertical=6),
                    border_radius=20,
                )
            )
        return ft.Row(chips, wrap=True, spacing=8, run_spacing=8)

    def build_center_card(center):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    center["name"],
                                    weight=ft.FontWeight.BOLD,
                                    size=16,
                                    expand=True,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.PHONE,
                                    icon_color=ft.Colors.GREEN_600,
                                    tooltip=f"تماس با {center['phone']}",
                                    data=center,
                                    on_click=open_phone_call,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.LOCATION_ON,
                                    icon_color=ft.Colors.RED_600,
                                    tooltip="مشاهده مسیر روی نقشه",
                                    data=center,
                                    on_click=open_map_route,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Text(
                            center["address"], size=13, color=ft.Colors.GREY_700
                        ),
                        ft.Text(
                            f"📞 {center['phone']}",
                            size=13,
                            color=ft.Colors.GREEN_700,
                        ),
                        ft.Divider(height=12),
                        ft.Text(
                            "خدمات این مرکز:",
                            size=13,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.TEAL_700,
                        ),
                        ft.Container(height=5),
                        build_services_row(center.get("services")),
                    ],
                    spacing=4,
                ),
                padding=12,
            )
        )

    centers_content = ft.Column(
        [
            ft.Text(
                "آدرس مراکز بهداشتی",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
            ),
            ft.Text(
                "مرکز بهداشت غرب کرج",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.GREEN_700,
            ),
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
        selected_index=0,
    )

    page.add(
        ft.Container(
            content=content_area,
            padding=20,
            alignment=ft.Alignment.TOP_RIGHT,
        )
    )


if __name__ == "__main__":
    ft.run(main)
