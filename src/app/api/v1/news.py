from fastapi import APIRouter
import random

router = APIRouter(tags=["news"])

class NewsItem:
    id: str
    img: str
    title: str
    time: str
    topic: str
    url: str

newsItems = [
    {'id': '1', 'img': 'https://photo.roscongress.org/api/structure/photos/374f99c7-72e5-4e38-a8d8-54b44bd805cb/preview', 'title': 'Форум по экономическим вопросам', 'time': '25 минут назад', 'topic': 'Экономика', 'url': 'https://photo.roscongress.org/api/structure/photos/374f99c7-72e5-4e38-a8d8-54b44bd805cb/preview'},
    {'id': '2', 'img': 'https://mff.minfin.ru/upload/iblock/b3b/6boxt0a1m9zy4vm1gtjaqnfmet1y0pqd/IMG_4832.JPG', 'title': 'Обсуждение бюджета на 2025 год', 'time': '30 минут назад', 'topic': 'Бюджет', 'url': 'https://mff.minfin.ru/upload/iblock/b3b/6boxt0a1m9zy4vm1gtjaqnfmet1y0pqd/IMG_4832.JPG'},
    {'id': '3', 'img': 'https://mff.minfin.ru/upload/iblock/f79/pmxdi7i9hz8yv9ws8j4dku04piadp9vf/1L4A0467.JPG', 'title': 'Встреча с инвесторами', 'time': '1 час назад', 'topic': 'Инвестиции', 'url': 'https://mff.minfin.ru/upload/iblock/f79/pmxdi7i9hz8yv9ws8j4dku04piadp9vf/1L4A0467.JPG'},
    {'id': '4', 'img': 'https://mff.minfin.ru/upload/iblock/1e8/h2sabpmlh7ga4ehk13xc2c11jjwv9nj6/IMG_5307.jpg', 'title': 'Презентация новых финансовых инструментов', 'time': '2 часа назад', 'topic': 'Финансовые инструменты', 'url': 'https://mff.minfin.ru/upload/iblock/1e8/h2sabpmlh7ga4ehk13xc2c11jjwv9nj6/IMG_5307.jpg'},
    {'id': '5', 'img': 'https://photo.roscongress.org/api/structure/photos/90634b5c-ce0e-4332-805f-1a3a866a293c/preview', 'title': 'Сессия по цифровым технологиям в экономике', 'time': '3 часа назад', 'topic': 'Цифровизация', 'url': 'https://photo.roscongress.org/api/structure/photos/90634b5c-ce0e-4332-805f-1a3a866a293c/preview'},
    {'id': '6', 'img': 'https://img.freepik.com/premium-photo/creative-growing-arrows-chart-blurry-city-texture-return-investment-finance-market-growth-concept-double-exposure_670147-17237.jpg?ga=GA1.1.562431132.1730131585&semt=ais_hybrid', 'title': 'Рост инвестиций в финансовом секторе', 'time': '4 часа назад', 'topic': 'Инвестиции', 'url': 'https://img.freepik.com/premium-photo/creative-growing-arrows-chart-blurry-city-texture-return-investment-finance-market-growth-concept-double-exposure_670147-17237.jpg?ga=GA1.1.562431132.1730131585&semt=ais_hybrid'},
    {'id': '7', 'img': 'https://img.freepik.com/free-vector/financial-incline-growth-upward-arrow-trend-background-design_1017-27107.jpg?ga=GA1.1.562431132.1730131585&semt=ais_hybrid', 'title': 'Тренды роста экономики в 2024 году', 'time': '5 часов назад', 'topic': 'Экономика', 'url': 'https://img.freepik.com/free-vector/financial-incline-growth-upward-arrow-trend-background-design_1017-27107.jpg?ga=GA1.1.562431132.1730131585&semt=ais_hybrid'},
    {'id': '8', 'img': 'https://img.freepik.com/premium-photo/pen-paper-with-price-quotes-charts-dynamics-their-change-coins_494741-42135.jpg?w=2000', 'title': 'Анализ рыночных котировок и динамики цен', 'time': '6 часов назад', 'topic': 'Финансовые рынки', 'url': 'https://img.freepik.com/premium-photo/pen-paper-with-price-quotes-charts-dynamics-their-change-coins_494741-42135.jpg?w=2000'},
    {'id': '9', 'img': 'https://img.freepik.com/premium-photo/technology-finance-concept_700248-33215.jpg?w=2000', 'title': 'Технологии в финансах и их влияние на рынок', 'time': '7 часов назад', 'topic': 'Технологии и финансы', 'url': 'https://img.freepik.com/premium-photo/technology-finance-concept_700248-33215.jpg?w=2000'},
    {'id': '10', 'img': 'https://img.freepik.com/premium-photo/young-businessman-mobile-phone_700248-32742.jpg?w=2000', 'title': 'Молодые предприниматели и новые идеи в бизнесе', 'time': '8 часов назад', 'topic': 'Предпринимательство', 'url': 'https://img.freepik.com/premium-photo/young-businessman-mobile-phone_700248-32742.jpg?w=2000'}
]

@router.get("/news")
async def get_random_news():
    random_news = random.sample(newsItems, 7)
    return random_news
