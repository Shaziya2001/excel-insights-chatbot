class Visualization:
    def create_bar_chart(self, data, x_column, y_column, title="Bar Chart", xlabel="X-axis", ylabel="Y-axis"):
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))
        plt.bar(data[x_column], data[y_column], color='blue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def create_line_chart(self, data, x_column, y_column, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 6))
        plt.plot(data[x_column], data[y_column], marker='o', color='green')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()