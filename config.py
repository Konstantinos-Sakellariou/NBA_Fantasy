def x_paths_generator(row: int):
    # Table 1 for Ranking, Player name and team
    table_body_left = '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[1]/div/table/tbody/'

    # Table 2 for the rest of player stats
    table_body_right = '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[3]/div[1]/div/div/div[2]/table/tbody/'

    # Define all XPATHS
    x_path_rk = f'{table_body_left}tr[{row}]/td[1]'
    xpath_pl_name = f'{table_body_left}tr[{row}]/td[2]/div/a'
    xpath_team = f'{table_body_left}tr[{row}]/td[2]/div/span'

    xpath_pos = f'{table_body_right}tr[{row}]/td[1]/div'
    x_path_games = f'{table_body_right}tr[{row}]/td[2]'
    xpath_min = f'{table_body_right}tr[{row}]/td[3]'
    xpath_points = f'{table_body_right}tr[{row}]/td[4]'
    xpath_fgm = f'{table_body_right}tr[{row}]/td[5]'
    xpath_fga = f'{table_body_right}tr[{row}]/td[6]'
    xpath_fg_perc = f'{table_body_right}tr[{row}]/td[7]'
    xpath_3pm = f'{table_body_right}tr[{row}]/td[8]'
    xpath_3pa = f'{table_body_right}tr[{row}]/td[9]'
    xpath_3p_perc = f'{table_body_right}tr[{row}]/td[10]'
    xpath_ftm = f'{table_body_right}tr[{row}]/td[11]'
    xpath_fta = f'{table_body_right}tr[{row}]/td[12]'
    xpath_ft_perc = f'{table_body_right}tr[{row}]/td[13]'
    xpath_reb = f'{table_body_right}tr[{row}]/td[14]'
    xpath_ass = f'{table_body_right}tr[{row}]/td[15]'
    xpath_stl = f'{table_body_right}tr[{row}]/td[16]'
    xpath_bls = f'{table_body_right}tr[{row}]/td[17]'
    xpath_to = f'{table_body_right}tr[{row}]/td[18]'
    xpath_dd2 = f'{table_body_right}tr[{row}]/td[19]'
    xpath_td3 = f'{table_body_right}tr[{row}]/td[20]'
    xpath_per = f'{table_body_right}tr[{row}]/td[21]'

    path_dict = {"ranking": x_path_rk,
                 "player_name": xpath_pl_name,
                 "team_abr": xpath_team,
                 "position": xpath_pos,
                 "games_played": x_path_games,
                 "minutes": xpath_min,
                 "points": xpath_points,
                 "field_goals_made": xpath_fgm,
                 "field_goals_attempted": xpath_fga,
                 "field_goals_percentage": xpath_fg_perc,
                 "three_pointers_made": xpath_3pm,
                 "three_pointers_attempted": xpath_3pa,
                 "three_pointers_percentage": xpath_3p_perc,
                 "free_throws_made": xpath_ftm,
                 "free_throws_attempted": xpath_fta,
                 "free_throws_percentage": xpath_ft_perc,
                 "rebounds": xpath_reb,
                 "assists": xpath_ass,
                 "steals": xpath_stl,
                 "blocks": xpath_bls,
                 "turnovers": xpath_to,
                 "double_doubles": xpath_dd2,
                 "triple_doubles": xpath_td3,
                 # "player_efficiency_rating": xpath_per
                 }

    return path_dict
