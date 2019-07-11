## tastytrade
Automatically gives dates and premiums to take profits based on average days held. Based off of the ['Should I Stay or Should I Go?'](https://www.tastytrade.com/tt/shows/market-measures/episodes/should-i-stay-or-should-i-go-07-30-2014) segment.

## Motivation
I got tired of figuring out the dates and percentages manually.
 
## Screenshots
![screenshot](https://github.com/jgrovedev/tastytrade/blob/master/tt.png)
![screenshot](https://github.com/jgrovedev/tastytrade/blob/master/example1.png)

## Tech/framework used
<b>Built with</b>
- [Python](https://www.python.org/) 
- [Datetime](https://docs.python.org/2/library/datetime.html)
- [Tabulate](https://pypi.org/project/tabulate/)

## Features
Automatically does the following:
- Generates the dates and premiums to take profits based on average days held.
- Exports table information to a text document for future reference.
- Prints 1/3 width of strikes (1-10) for quick reference.
- Gives date 21 days prior to expiration to exit trade.

## How to use?
Simply enter 'width' to view how much premium should be collected per 1/3 width of strikes. Enter 'position' and enter requested information to export profit table.
