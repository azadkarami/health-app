import flet as ft

def main(page: ft.Page):
    page.title = "مرکز بهداشت"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    page.appbar = ft.AppBar(
        title=ft.Text("مرکز بهداشت شهر من", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_700,
        center_title=True
    )

    rabies_content = ft.Column([
        ft.Text("آموزش بیماری هاری", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
        ft.Text("هاری یک بیماری ویروسی کشنده است که سیستم عصبی مرکزی را هدف می‌گیرد.", size=16),
        ft.Container(height=10),
        ft.ExpansionTile(
            title=ft.Text("راه‌های انتقال", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Text("از طریق بزاق حیوان آلوده، گاز گرفتن، خراش یا لیسیدن زخم باز و مخاط چشم و دهان منتقل می‌شود.")
            ]
        ),
        ft.ExpansionTile(
            title=ft.Text("علائم هشدار", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Text("تب، سردرد، اضطراب، توهم، ترس شدید از آب (هیدروفوبیا) و تشنج. این مرحله نقطه بدون بازگشت است.")
            ]
        ),
        ft.ExpansionTile(
            title=ft.Text("اقدام فوری پس از گزش", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Text("۱. شست‌وشوی فوری زخم با آب و صابون به مدت ۱۵ دقیقه\n۲. ضدعفونی با بتادین یا الکل\n۳. مراجعه فوری به بیمارستان برای دریافت واکسن هاری و ایمونوگلوبولین")
            ]
        ),
        ft.ExpansionTile(
            title=ft.Text("پیشگیری", weight=ft.FontWeight.BOLD),
            controls=[
                ft.Text("واکسیناسیون حیوانات خانگی، فاصله گرفتن از حیوانات وحشی و ولگرد، و گزارش فوری هر گزش به مراکز بهداشت.")
            ]
        )
    ])

    centers_content = ft.Column([
        ft.Text("آدرس مراکز بهداشتی", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ft.Text("برای دریافت خدمات و واکسن هاری به نزدیک‌ترین مرکز مراجعه کنید:", size=16),
        ft.Container(height=10),
        ft.Card(content=ft.ListTile(leading=ft.Icon(ft.Icons.LOCATION_ON), title=ft.Text("مرکز بهداشت شماره ۱"), subtitle=ft.Text("خیابان اصلی، پلاک ۱۰ - تلفن: ۰۲۱۱۲۳۴۵۶۷"))),
        ft.Card(content=ft.ListTile(leading=ft.Icon(ft.Icons.LOCATION_ON), title=ft.Text("مرکز بهداشت شماره ۲"), subtitle=ft.Text("میدان انقلاب، جنب بیمارستان - تلفن: ۰۲۱۷۶۵۴۳۲۱"))),
        ft.Card(content=ft.ListTile(leading=ft.Icon(ft.Icons.LOCATION_ON), title=ft.Text("مرکز بهداشت شماره ۳"), subtitle=ft.Text("خیابان شهید بهشتی، کوچه گلستان - تلفن: ۰۲۱۹۸۷۶۵۴۳"))),
    ])

    content_area = ft.Column(expand=True)

    def on_nav_change(e):
        index = e.control.selected_index
        content_area.controls.clear()
        if index == 0:
            content_area.controls.append(
                ft.Column([
                    ft.Text("به اپلیکیشن سلامت خوش آمدید", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                    ft.Container(height=10),
                    ft.Text("از منوی پایین می‌توانید به بخش‌های آموزش هاری و آدرس مراکز دسترسی داشته باشید.", size=16)
                ])
            )
        elif index == 1:
            content_area.controls.append(rabies_content)
        elif index == 2:
            content_area.controls.append(centers_content)
        page.update()

    content_area.controls.append(
        ft.Column([
            ft.Text("به اپلیکیشن سلامت خوش آمدید", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
            ft.Container(height=10),
            ft.Text("از منوی پایین می‌توانید به بخش‌های آموزش هاری و آدرس مراکز دسترسی داشته باشید.", size=16)
        ])
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="خانه"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="آموزش هاری"),
            ft.NavigationBarDestination(icon=ft.Icons.LOCATION_ON, label="آدرس مراکز"),
        ],
        on_change=on_nav_change,
        selected_index=0
    )

    page.add(
        ft.Container(content=content_area, padding=20, alignment=ft.Alignment.TOP_RIGHT)
    )

ft.run(main)
