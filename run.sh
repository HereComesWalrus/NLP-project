sed '/^cobr.r?/d;
	/^?/d; 
	/^n-[eé]-verbo/d;
	/^.*[cC]obrem.*cobrem.*\./d;
	/^cobrir/ s/[cC]obrem/cobrir/;
	/^cobrar/ s/[cC]obrem/cobrar/;
	s/^cobr.r\t//;
	' cobremCobrarCobrir.out> cobremCobrarCobrir.final

sed '/^ver?/d;  
	/^vestir?/d;  
	/^?/d;  
	/^n-[eé]-verbo/d; 
	/^.*[vV]isto.*visto.*\./d;
	/^ver/ s/[vV]isto/ver/;
	/^vestir/ s/[vV]isto/vestir/;
	s/^ver//;
	s/^vestir\t//;' vistoVerVestir-2.out > vistoVerVestir-2.final


