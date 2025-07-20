import argparse
import csv
import matplotlib.pyplot as plt
import os

def parse_file(filename):
    """Функция для чтения данных из файлов разных форматов"""
    ext = os.path.splitext(filename)[1].lower()
    
    x = []
    y = []
    
    try:
        if ext == '.csv':
           with open(filename) as f:
                reader = csv.reader(f)
                next(reader) 
                for row in reader:
                    x.append(float(row[1]))
                    y.append(float(row[2]))
    
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None
    
    return x, y

def plot_graph(x, y, args):
    """Функция для построения графика с заданными параметрами"""
    plt.figure(figsize=args.figsize if args.figsize else (10, 6))
    

    linestyle = '-'
    if args.linestyle:
        styles = {'solid': '-', 'dashed': '--', 'dotted': ':'}
        linestyle = styles.get(args.linestyle, '-')
    
  
    line, = plt.plot(x, y, 
                    linestyle=linestyle,
                    linewidth=args.linewidth if args.linewidth else 2,
                    color=args.color if args.color else 'b',
                    label=args.legend if args.legend else None)
    

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
    if hasattr(args, 'xticks') and args.xticks:
        plt.xticks(ticks=args.xticks)
    if hasattr(args, 'yticks') and args.yticks:
        plt.yticks(ticks=args.yticks)
    if args.grid is not None:
        plt.grid(args.grid)
    if args.fill:
        plt.fill_between(x, y, alpha=0.2)
    if args.legend:
        plt.legend()
    

    if args.output:
        plt.savefig(args.output)
        print(f"График сохранен в файл: {args.output}")
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description='Программа для построения графиков из файлов данных')
    

    parser.add_argument('filename', help='Имя файла с данными')
    
    parser.add_argument('--legend', help='Текст для легенды на графике')
    
    parser.add_argument('--output', help='Имя файла для сохранения графика')
    
    args = parser.parse_args()

    x, y = parse_file(args.filename)
    
    if x and y:
  
        plot_graph(x, y, args)
    else:
        print("Не удалось прочитать данные из файла")

if __name__ == '__main__':
    main()
