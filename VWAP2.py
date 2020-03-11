"""        # There are five steps in calculating VWAP:
 
         #
 
         # Calculate the Typical Price for the period. [(High + Low + Close)/3)]
 
         #
 
         # Multiply the Typical Price by the period Volume (Typical Price x Volume)
 
         #
 
         # Create a Cumulative Total of Typical Price. Cumulative(Typical Price x Volume)
 
         #
 
         # Create a Cumulative Total of Volume. Cumulative(Volume)
 
         #
 
         # Divide the Cumulative Totals.
 
         #
 
         # VWAP = Cumulative(Typical Price x Volume) / Cumulative(Volume)
 
"""
import backtrader as bt


class VolumeWeightedAveragePrice(bt.Indicator):

    alias = (
        "VWAP",
        "VolumeWeightedAveragePrice",
    )
    lines = ("vwap",)
    params = (("period", 5),)

    plotinfo = dict(subplot=False)

    def __init__(self):

        self.addminperiod(self.p.period)
        self.cum_price_by_Volume = list()
        self.cum_volume = list()

    def _plotlabel(self):

        # This method returns a list of labels that will be displayed
        # behind the name of the indicator on the plot

        # The period must always be there

        plabels = [self.p.period]

        plabels += [self.lines.vwap]
        return plabels

    def next(self):

        # print(dir(self.data))

        price = (self.data.close + self.data.high + self.data.low) / 3

        # check price
        print(price)

        volume = self.data.volume
        # check price
        print(volume)

        price_by_Volume = price * volume

        self.cum_price_by_Volume.append(price_by_Volume)
        self.cum_volume.append(volume)

        if len(self.cum_price_by_Volume) and len(self.cum_volume) >= self.p.period:

            # Check cumulative values for accuracy

            print(sum(self.cum_price_by_Volume[-1 * (self.p.period) :]))
            print(sum(self.cum_volume[-1 * (self.p.period) :]))

            # get last n'th (period) values in list and perform calculations for VWAP. This is because
            # the latest values go at the end of the list due to the way data is imported (earliest to latest)

            self.lines.vwap[0] = sum(
                self.cum_price_by_Volume[-1 * (self.p.period) :]
            ) / sum(self.cum_volume[-1 * (self.p.period) :])

