def filter_row_tds(row_td):
    row_td_classes = row_td.get('class') or []
    row_td_classes_set = set(row_td_classes)
    # print('row_td_classes', row_td_classes)

    custom_classes = {'poz', 'echipa', 'puncte'}
    set_intersection = row_td_classes_set.intersection(custom_classes)
    # print('set_intersection', len(set_intersection), set_intersection)

    has_my_class = len(set_intersection) > 0
    has_image = row_td.find('img') is not None
    is_without_class = len(row_td_classes) == 0

    return has_my_class or has_image or is_without_class


def map_team_data(team_data):
    if team_data.text != '':
        return team_data.text

    return team_data.find('img').get('data-src')


def get_team_from_table_row(html_row):
    cols = ['position', 'logo', 'name', 'matches', 'gd', 'points']
    row_tds = html_row.findAll('td')
    row_tds = list(filter(filter_row_tds, row_tds))
    team_data = list(map(map_team_data, row_tds))
    # print('team_data', team_data)

    return dict(zip(cols, team_data))
