import random
import math

# 각 도시의 좌표
cities = {'A': (0, 3), 'B': (7, 5), 'C': (6, 0), 'D': (4, 3),
          'E': (1, 0), 'F': (5, 3), 'H': (4, 1), 'G': (2, 2)}

# 알고리즘 파라미터
population_size = 8
crossover_ratio = 1.0
mutation_ratio = 0.01

# 거리 계산 함수
def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += math.dist(cities[city1], cities[city2])
    return total_distance

# 초기 개체 생성 함수
def generate_individual():
    cities_list = list(cities.keys())
    random.shuffle(cities_list)
    return cities_list

# 사이클 교차 연산 함수
def cycle_crossover(parent1, parent2):
    cycle = [-1] * len(parent1)
    index = 0

    while cycle[index] == -1:
        cycle[index] = parent1[index]
        index = parent2.index(parent1[index])

    child1 = [parent1[i] if parent1[i] in cycle else parent2[i] for i in range(len(parent1))]
    child2 = [parent2[i] if parent2[i] in cycle else parent1[i] for i in range(len(parent2))]

    return child1, child2

# 돌연변이 함수
def mutate(individual):
    if random.random() < mutation_ratio:
        # 두 도시의 위치를 무작위로 교환
        mutation_point1, mutation_point2 = random.sample(range(len(individual)), 2)
        individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
    return individual

# 선택 함수
def selection(population):
    # 토너먼트 선택 사용
    tournament_size = 3
    selected = random.sample(population, tournament_size)
    return min(selected, key=lambda x: calculate_distance(x))

# 초기 인구 생성
population = [generate_individual() for _ in range(population_size)]

# 최대 반복 횟수 설정
max_generations = 100

for generation in range(max_generations):
    # 새로운 세대 생성
    new_population = []

    # 교차 연산
    for _ in range(int(crossover_ratio * population_size / 2)):
        parent1 = selection(population)
        parent2 = selection(population)
        child1, child2 = cycle_crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])

    # 나머지 개체는 직전 세대에서 선택
    remaining_size = population_size - len(new_population)
    new_population.extend([mutate(selection(population)) for _ in range(remaining_size)])

    # 새로운 세대로 갱신
    population = new_population

# 최적 경로 출력
best_route = min(population, key=lambda x: calculate_distance(x))
best_route+=best_route[0]
best_distance = calculate_distance(best_route)

print("최적 경로:", best_route)
print("이동 거리:", best_distance)
