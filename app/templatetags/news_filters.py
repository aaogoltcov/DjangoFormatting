from datetime import datetime, timedelta

from django import template


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    minutes = int((datetime.timestamp(datetime.today()) - value) / 60)
    if minutes <= 10:
        return "только что"
    elif 10 < minutes <= (24 * 60):
        return f'{int(minutes / 60)} часов назад'
    else:
        return datetime.fromtimestamp(value)


# необходимо добавить фильтр для поля `score`
@register.filter
def get_score(value, default=None):
    try:
        if int(value) < -5:
            return 'все плохо'
        elif -5 <= int(value) < 5:
            return 'нейтрально'
        else:
            return 'хорошо'
    except ValueError:
        return default


@register.filter
def format_num_comments(value):
    # Ваш код
    if int(value) == 0:
        return 'оставьте комментарий'
    elif 0 < int(value) <= 50:
        return int(value)
    else:
        return '50+'

@register.filter
def format_selftext(selftext, count=0):
    selftext_by_words = selftext.split()
    if int(count) >= len(selftext_by_words) or int(count) == 0:
        return selftext
    else:
        start_of_sentence = ' '.join(word for word in selftext_by_words[0:(int(count) - 1)])
        end_of_sentence = ' '.join(word for word in selftext_by_words[-(int(count)):-1])
        return f'{start_of_sentence} ... {end_of_sentence}'
