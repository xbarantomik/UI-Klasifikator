import time
import matplotlib.pyplot as plt
import math
import random

#....konstanty.....................................................................................
n = 10

k_list = [1, 3, 7, 15]
k_list_count = [0, 0, 0, 0]
dtset = 51


#....do listu classes sa ukladaju vsetky triedy pre vsetky k.......................................
            # k = 1
classes = [{0: [[-45*n, -44*n], [-41*n, -30*n], [-18*n, -24*n], [-25*n, -34*n], [-20*n, -14*n]],    #RED
            1: [[+45*n, -44*n], [+41*n, -30*n], [+18*n, -24*n], [+25*n, -34*n], [+20*n, -14*n]],    #GREEN
            2: [[-45*n, +44*n], [-41*n, +30*n], [-18*n, +24*n], [-25*n, +34*n], [-20*n, +14*n]],    #BLUE
            3: [[+45*n, +44*n], [+41*n, +30*n], [+18*n, +24*n], [+25*n, +34*n], [+20*n, +14*n]]},   #PURPLE

           # k = 3
           {0: [[-45*n, -44*n], [-41*n, -30*n], [-18*n, -24*n], [-25*n, -34*n], [-20*n, -14*n]],    #RED
            1: [[+45*n, -44*n], [+41*n, -30*n], [+18*n, -24*n], [+25*n, -34*n], [+20*n, -14*n]],    #GREEN
            2: [[-45*n, +44*n], [-41*n, +30*n], [-18*n, +24*n], [-25*n, +34*n], [-20*n, +14*n]],    #BLUE
            3: [[+45*n, +44*n], [+41*n, +30*n], [+18*n, +24*n], [+25*n, +34*n], [+20*n, +14*n]]},   #PURPLE

           # k = 7
           {0: [[-45*n, -44*n], [-41*n, -30*n], [-18*n, -24*n], [-25*n, -34*n], [-20*n, -14*n]],    #RED
            1: [[+45*n, -44*n], [+41*n, -30*n], [+18*n, -24*n], [+25*n, -34*n], [+20*n, -14*n]],    #GREEN
            2: [[-45*n, +44*n], [-41*n, +30*n], [-18*n, +24*n], [-25*n, +34*n], [-20*n, +14*n]],    #BLUE
            3: [[+45*n, +44*n], [+41*n, +30*n], [+18*n, +24*n], [+25*n, +34*n], [+20*n, +14*n]]},   #PURPLE

           # k = 15
           {0: [[-45*n, -44*n], [-41*n, -30*n], [-18*n, -24*n], [-25*n, -34*n], [-20*n, -14*n]],    #RED
            1: [[+45*n, -44*n], [+41*n, -30*n], [+18*n, -24*n], [+25*n, -34*n], [+20*n, -14*n]],    #GREEN
            2: [[-45*n, +44*n], [-41*n, +30*n], [-18*n, +24*n], [-25*n, +34*n], [-20*n, +14*n]],    #BLUE
            3: [[+45*n, +44*n], [+41*n, +30*n], [+18*n, +24*n], [+25*n, +34*n], [+20*n, +14*n]]}]   #PURPLE


#....vyp. vzdialenosti od bodov, k najkratsich porovna a klasifikuje triedu........................
def classify(x, y, k, k_class):

    distance = []
    for class_ in k_class:
        for point in k_class[class_]:
            dist = math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
            distance.append([round(dist, 3), class_])

    distance_sorted = sorted(distance)[:k]

    # red, green, blue, purple
    r_g_b_p = [0, 0, 0, 0]

    for d in distance_sorted:
        if d[1] == 0:
            r_g_b_p[0] += 1
        elif d[1] == 1:
            r_g_b_p[1] += 1
        elif d[1] == 2:
            r_g_b_p[2] += 1
        elif d[1] == 3:
            r_g_b_p[3] += 1

    max_num = max(r_g_b_p)
    if max_num == r_g_b_p[0]:
        return 'r', 0
    elif max_num == r_g_b_p[1]:
        return 'g', 1
    elif max_num == r_g_b_p[2]:
        return 'b', 2
    elif max_num == r_g_b_p[3]:
        return 'p', 3


#....vytvorenie noveho botu, tak aby neboli 2 na rovnakej pozicii..................................
def generate_coordinates(x_lim_1, x_lim_2, y_lim_1, y_lim_2):
    x = random.randint(x_lim_1, x_lim_2)
    y = random.randint(y_lim_1, y_lim_2)
    while 1:
        check = 0
        for class_ in classes[0]:
            #classes[0] preto, lebo suradnice su pri kazdom k roznake aj sa ptm nove x,y prida do kazdej (trieda bude len ina)
            for point in classes[0][class_]:
                if point[0] == x and point[1] == y:
                    if point[0] == x and point[1] == y:
                        x = random.randint(x_lim_1, x_lim_2)
                        y = random.randint(y_lim_1, y_lim_2)
                    elif point[0] == x:
                        x = random.randint(x_lim_1, x_lim_2)
                    else:
                        y = random.randint(y_lim_1, y_lim_2)
                    check += 1
                    break
            if check != 0:
                break
        if check != 0:
            continue
        else:
            break
    return x, y


#....pre vsetky k sa zavola clasify() a porovna sa v originalnou triedou...........................
def compare(class_, x, y):
    for k in range(len(k_list)):
        the_class, class_num = classify(x, y, k_list[k], classes[k])
        if the_class == class_:
            k_list_count[k] += 1
        classes[k][class_num].append([x, y])


#....vypocitanie uspesnosti klasifikatora..........................................................
def calculate_results(k):
    suc = k_list_count[k]
    omega = len(k_list)*dtset*n
    fin = suc / (omega / 100)
    return fin


#....vykraslenie grafu pre kazde k.................................................................
def create_graph():
    r_x = []
    r_y = []
    g_x = []
    g_y = []
    b_x = []
    b_y = []
    p_x = []
    p_y = []
    for k in range(len(k_list)):
        for i in classes[k][0]:
            r_x.append(i[0])
            r_y.append(i[1])

        for i in classes[k][1]:
            g_x.append(i[0])
            g_y.append(i[1])

        for i in classes[k][2]:
            b_x.append(i[0])
            b_y.append(i[1])

        for i in classes[k][3]:
            p_x.append(i[0])
            p_y.append(i[1])

        plt.scatter(r_x, r_y, 10, color=['red'])
        plt.scatter(g_x, g_y, 10, color=['green'])
        plt.scatter(b_x, b_y, 10, color=['blue'])
        plt.scatter(p_x, p_y, 10, color=['purple'])

        plt.xlabel('x - axis')
        plt.ylabel('y - axis')

        result = calculate_results(k)
        print(f"k = {k_list[k]}: {round(result, 2)}%")
        print(f"All: {4*dtset*n}\nCorrect: {k_list_count[k]}\n")

        plt.title(f'k = {str(k_list[k])}   |   {round(result, 2)}%')
        plt.xlim([-50*n, 50*n])
        plt.ylim([-50*n, 50*n])
        plt.show()


#....main..........................................................................................
def main():
    global classes
    time_start = time.perf_counter()
    prob_99 = round(0.99 * dtset*n)
    prob_1 = round(0.01 * dtset*n)
    # cyklus pre 99% bodov (s obmedzenymi hranicami novych bodov)
    for i in range(prob_99):
        # print(i)

        # red 99%
        x, y = generate_coordinates(-50*n, 5*n, -50*n, 5*n)
        compare('r', x, y)
        del x, y
        # green 99%
        x, y = generate_coordinates(-5*n, 50*n, -50*n, 5*n)
        compare('g', x, y)
        # blue 99%
        x, y = generate_coordinates(-50*n, 5*n, -5*n, 50*n)
        compare('b', x, y)
        del x, y
        # purple 99%
        x, y = generate_coordinates(-5*n, 50*n, -5*n, 50*n)
        compare('p', x, y)
        del x, y

    # cyklus pre 1% bodov (bez obmedzenych hranic novych bodov)
    for i in range(prob_1):
        # print(prob_99 + i)

        # red 1%
        x, y = generate_coordinates(-50*n, 50*n, -50*n, 50*n)
        compare('r', x, y)
        del x, y
        # green 1%
        x, y = generate_coordinates(-50*n, 50*n, -50*n, 50*n)
        compare('g', x, y)
        del x, y
        # blue 1%
        x, y = generate_coordinates(-50*n, 50*n, -50*n, 50*n)
        compare('b', x, y)
        del x, y
        # purple 1%
        x, y = generate_coordinates(-50*n, 50*n, -50*n, 50*n)
        compare('p', x, y)
        del x, y

    time_end = time.perf_counter()
    create_graph()
    print(f"Time: {round((time_end - time_start)/60, 1) }min [{round((time_end - time_start), 1)} s] ")


if __name__ == '__main__':
    main()
