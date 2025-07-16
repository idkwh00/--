import argparse
import json
import csv
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os

def parse_file(filename):
    """Функция для чтения данных из файлов разных форматов"""
    ext = os.path.splitext(filename)[1].lower()
    
    x = []
    y = []
    
    try:
        if ext == '.json':
            with open(filename) as f:
                data = json.load(f)
                if 'data' in data:  # Формат 4
                    for item in data['data']:
                        x.append(item['x'])
                        y.append(item['y'])
                else:  # Формат 3
                    x = data['x']
                    y = data['y']
        
        elif ext == '.csv':
            with open(filename) as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    x.append(float(row[1]))
                    y.append(float(row[2]))
        
        elif ext == '.txt':
            with open(filename) as f:
                for line in f:
                    parts = line.strip().split('    ')
                    if len(parts) == 2:
                        x.append(float(parts[0]))
                        y.append(float(parts[1]))
        
        elif ext == '.xml':
            tree = ET.parse(filename)
            root = tree.getroot()
            
            # Проверяем формат XML (5 или 6)
            if root.find('xdata') is not None:  # Формат 5
                xdata = root.find('xdata')
                ydata = root.find('ydata')
                for xval in xdata.findall('x'):
                    x.append(float(xval.text))
                for yval in ydata.findall('y'):
                    y.append(float(yval.text))
            else:  # Формат 6
                for row in root.findall('row'):
                    x.append(float(row.find('x').text))
                    y.append(float(row.find('y').text))
    
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None
    
    return x, y

def plot_graph(x, y, args):
    """Функция для построения графика с заданными параметрами"""
    plt.figure(figsize=args.figsize if args.figsize else (10, 6))
    
    # Определяем стиль линии
    linestyle = '-'
    if args.linestyle:
        styles = {'solid': '-', 'dashed': '--', 'dotted': ':'}
        linestyle = styles.get(args.linestyle, '-')
    
    # Строим график с параметрами
    line, = plt.plot(x, y, 
                    linestyle=linestyle,
                    linewidth=args.linewidth if args.linewidth else 2,
                    color=args.color if args.color else 'b',
                    label=args.legend if args.legend else None)
    
    # Устанавливаем параметры графика
    if args.title:
        plt.title(args.title)
    if args.xlabel:
        plt.xlabel(args.xlabel)
    if args.ylabel:
        plt.ylabel(args.ylabel)
    if args.xlim:
        plt.xlim(args.xlim[0], args.xlim[1])
    if args.ylim:
        plt.ylim(args.ylim[0], args.ylim[1])
    if args.xticks:
        plt.xticks(ticks=args.xticks)
    if args.yticks:
        plt.yticks(ticks=args.yticks)
    if args.grid is not None:
        plt.grid(args.grid)
    if args.fill:
        plt.fill_between(x, y, alpha=0.2)
    if args.legend:
        plt.legend()
    
    # Сохраняем или показываем график
    if args.output:
        plt.savefig(args.output)
        print(f"График сохранен в файл: {args.output}")
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description='Программа для построения графиков из файлов данных')
    
    # Обязательный аргумент - имя файла
    parser.add_argument('filename', help='Имя файла с данными (txt, csv, json, xml)')
    
    # Дополнительные параметры для варианта 13 (Текст для легенды на графике)
    parser.add_argument('--legend', help='Текст для легенды на графике')
    
    # Другие возможные параметры (для демонстрации)
    parser.add_argument('--title', help='Заголовок графика')
    parser.add_argument('--xlabel', help='Подпись оси X')
    parser.add_argument('--ylabel', help='Подпись оси Y')
    parser.add_argument('--xlim', nargs=2, type=float, help='Границы оси X (min max)')
    parser.add_argument('--ylim', nargs=2, type=float, help='Границы оси Y (min max)')
    parser.add_argument('--linestyle', choices=['solid', 'dashed', 'dotted'], help='Стиль линии')
    parser.add_argument('--linewidth', type=float, help='Толщина линии')
    parser.add_argument('--color', help='Цвет линии')
    parser.add_argument('--grid', action='store_true', help='Включить сетку')
    parser.add_argument('--no-grid', dest='grid', action='store_false', help='Выключить сетку')
    parser.add_argument('--fill', action='store_true', help='Заливка под кривой')
    parser.add_argument('--output', help='Имя файла для сохранения графика')
    parser.add_argument('--figsize', nargs=2, type=float, help='Размер графика (ширина высота)')
    
    args = parser.parse_args()
    
    # Читаем данные из файла
    x, y = parse_file(args.filename)
    
    if x and y:
        # Строим график
        plot_graph(x, y, args)
    else:
        print("Не удалось прочитать данные из файла")

if __name__ == '__main__':
    main()