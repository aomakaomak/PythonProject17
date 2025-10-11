from src.hh import HH
from src.save_to_json_file import SaveToJsonFile
from src.utils import get_top_n_for_keyword
from src.work_with_vacancies import WorkWithVacancies


def main_function():
    """Главная функция взаимодействия с пользователем."""
    kw = input("Введите ключевое слово для поиска на hh.ru: ").strip()
    if not kw:
        print("Пустой запрос.")
        return

    try:
        n = int(
            input(
                "Введите количество вакансий для вывода (топ N по зарплате): "
            ).strip()
        )
    except ValueError:
        print("Нужно ввести число.")
        return

    top_vacancies = get_top_n_for_keyword(kw, n)
    if not top_vacancies:
        print("Ничего не найдено.")
        return

    # выводим вакансии на экран
    print(f"\n— Топ-{n} по зарплате для «{kw}» —")
    for i, v in enumerate(top_vacancies, 1):
        print(f"{i}. {v['name']} — {v['salary']} ₽ | {v['link']}")

        # -------- Сохраняем через Save_to_json_file --------
    # 1) Получаем сырые данные с hh (те же по ключевому слову)
    hh = HH(file_worker=None)
    raw_all = hh.load_vacancies(kw)  # список «сырых» вакансий от API

    # 2) Оставляем только те, что попали в топ (по ссылкам)
    top_links = {v["link"] for v in top_vacancies}
    raw_selected = [v for v in raw_all if v.get("alternate_url") in top_links]

    # 3) Отдаём сырые вакансии в Save_to_json_file -> внутри они нормализуются и сохраняются
    file_path = f"data/top_{n}_{kw}.json"
    saver = SaveToJsonFile(raw_selected)
    saver.save_vacancies_in_file(file_path)

    print(f"\n✅ Топ-{n} вакансий сохранён в файл: {file_path}")


if __name__ == "__main__":
    main_function()
