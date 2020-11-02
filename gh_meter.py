"""Main module of program github-meter. For start program touch it.

"""
import time

import gh_meter_function as fn

import settings as st


k = True
l = False

while k or l:
    fn.print_main_menu()
    key=input("Your choice: ")
    if key == '0':
        print("\n" * 100)
        k = False
    elif key == '1':
        total_dict = fn.create_total_dict()
        data_count_sorted = fn.process_total_dict(total_dict)
        print ("\n" * 100)
        fn.create_total_count_table(data_count_sorted)

        while True:
            print("")
            ch = input("Do you want to create bar chart? (y/n): ")
            if ch == 'y':
                time.sleep(2)
                fn.create_total_count_chart(data_count_sorted)
                break
            elif ch == 'n':
                time.sleep(1)
                break

        fn.print_back_menu()
        l = True
        while l == True:
            key = input("Your choice: ")
            if key == '0':
                k,l = False, False
                print("\n" * 100)
            elif key == '1':
                l = False
    elif key == '3':
        users_tot_dict = fn.get_stat_users()
        list_users = fn.process_users(users_tot_dict)
        fn.create_users_table(list_users)

        fn.print_back_menu()
        l = True
        while l == True:
            key = input("Your choice: ")
            if key == '0':
                k,l = False, False
                print("\n" * 100)
            elif key == '1':
                l = False

    elif key == '2':
        print ("\n" * 100)
        print ("1.Look infomation about all pre-installing languages in file settings.py?")
        print ("2.Look information about other language or only one")
        print ("3.Main menu")
        print ("0.Exit")
        print ("")
        l = True
        while l == True:
            key = input ("Your choice: ")

            if key == '0':
                l = False
                k = False
            elif key == '3':
                l = False
            elif key == '2':
                print("\n" * 100)
                lang = input("How language do you want to see?: " )
                lang.lower()
                print("\n" * 100)

                lang_dict = fn.get_stat_from_github(lang)
                list_repos = fn.process_depos_lang(lang_dict)
                fn.create_sum_repos_table(list_repos, lang)

                while True:
                    print("")
                    ch = input("Do you want to get more detailed information in text? (y/n): ")
                    if ch == 'y':
                        time.sleep(2)
                        fn.output_info_depos(list_repos)
                        break
                    elif ch == 'n':
                        time.sleep(1)
                        break

                while True:
                    print("")
                    ch = input("Do you want to create bar chart? (y/n): ")
                    if ch == 'y':
                        time.sleep(2)
                        fn.create_repos_lang_chart(list_repos, lang)
                        break
                    elif ch == 'n':
                        time.sleep(1)
                        break

                fn.print_back_menu()
                l = True
                while l == True:
                    key = input("Your choice: ")
                    if key == '0':
                        k,l = False, False
                        print("\n" * 100)
                    elif key == '1':
                        l = False
            elif key == '1':
                print("\n" * 100)
                tot_dict = fn.create_total_dict()
                for language in st.list_languages:
                    lang_dict = tot_dict[language]
                    list_repos = fn.process_depos_lang(lang_dict)
                    fn.create_sum_repos_table(list_repos, language)
                    fn.create_repos_lang_chart(list_repos, language)

                fn.print_back_menu()
                l = True
                while l == True:
                    key = input("Your choice: ")
                    if key == '0':
                        k,l = False, False
                        print("\n" * 100)
                    elif key == '1':
                        l = False
