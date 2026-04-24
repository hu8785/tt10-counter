## How it works

This project implements a 4-bit synchronous up counter.

The input is:
- enable

The clock is provided by Tiny Tapeout through clk, and reset is provided through rst_n.

When rst_n = 0, the counter resets to 0000.  
When rst_n = 1 and enable = 1, the counter increments by one on every rising edge of clk.  
When enable = 0, the counter holds its current value.

The output counter_out is 4 bits wide and counts from 0000 to 1111, which is 0 to 15 in decimal.

## How to test

First apply reset by setting rst_n = 0.  
Then release reset by setting rst_n = 1.  
After that, set enable = 1 and observe the output count increasing at each clock edge.  
When enable = 0, the counter should stop counting and hold its last value.

## External hardware

None

## Pinout

### Inputs
- ui[0] = enable

### Outputs
- uo[0] = counter_out[0]
- uo[1] = counter_out[1]
- uo[2] = counter_out[2]
- uo[3] = counter_out[3]
