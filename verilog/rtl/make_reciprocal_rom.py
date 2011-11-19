#
# For 0-1024, create a table that computes 1/x
# Assumed a normalized significand with an implicit leading one.
#

print '''
//
// This file is autogenerated by make_reciprocal_rom.py
//

module reciprocal_rom(
	input [9:0]			addr_i,
	output reg [9:0]	data_o);

	always @*
	begin
		case (addr_i)'''


for x in range(0, 1024):
	significand = 1024 | x
	reciprocal = int((1024 * 1024) / significand)
	print '\t\t\t10\'h%03x: data_o = 10\'h%03x;' % (x, reciprocal & 0x3ff),
	print '// 1 / ' + str(significand) + ' = ' + str(reciprocal)
	
print '''		endcase
	end
endmodule
'''