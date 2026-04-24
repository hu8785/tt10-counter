`default_nettype none

module tt_um_akanksha_hu8785_counter (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire enable = ui_in[0];

    reg [3:0] counter_out;

    always @(posedge clk) begin
        if (!rst_n)
            counter_out <= 4'b0000;
        else if (enable)
            counter_out <= counter_out + 1'b1;
    end

    assign uo_out[0] = counter_out[0];
    assign uo_out[1] = counter_out[1];
    assign uo_out[2] = counter_out[2];
    assign uo_out[3] = counter_out[3];
    assign uo_out[4] = 1'b0;
    assign uo_out[5] = 1'b0;
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    wire _unused = &{ena, ui_in[7:1], uio_in, 1'b0};

endmodule

`default_nettype wire
