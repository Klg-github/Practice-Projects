# Practice-Projects
Projects made by Karl Gorski

12/28/24 CSV Price Graph: Graphs price data from a csv file, colors segments where price increases as green and segments where price decreases as red. Can graph open, close, high, and low prices and choose the title. The CSV file must be formatted to have the Date, Open, Close, ect as the titles of the columns. I haven't added too many features such as being able to compare different sets of data such as the open and close times for the dates or the close prices for two different stocks. I also haven't made it the most user friendly so if an error is made while using the program, it will probably return a generic error. I put an example csv file that is formatted correctly for my code. 

1/6/25 Simple Strategy Backtest: The point of this project was to practice using python to backtest a strategy. The strategy is simply to take the mean close price of the previous five days and if today's close price is less than the mean then buy and if today's close price is higher than the mean then sell. This isn't really a good strategy obviously but I used it because it was easy to implement as the point of the project was backtesting. When used on SPX Data from the last year it returned -8.5%. Overall the purpose was to dip into this sort of programming project. Files are Backtest Practice Project.py, Backtest_Practice_Project_Functions.py, and Simple_Strategy.py. The data in SPX Data.csv works for this project and is what I used.
