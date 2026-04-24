import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start 4-bit Counter Test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset counter
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    # Release reset, enable low
    dut.rst_n.value = 1
    dut.ui_in[0].value = 0
    await ClockCycles(dut.clk, 10)

    # Enable counter
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 30)

    # Disable counter and hold
    dut.ui_in[0].value = 0
    await ClockCycles(dut.clk, 10)

    # Enable again
    dut.ui_in[0].value = 1
    await ClockCycles(dut.clk, 20)

    # Reset again
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)

    dut._log.info("4-bit Counter Test Completed")
