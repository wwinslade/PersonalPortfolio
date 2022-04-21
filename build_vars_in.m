%% Inputs
nTerms = 21 ; % Enter number of sims to run
varCount = 2 ; % Number of variables to write data for

% First Variable: Linker Stiffness
var1Min = 0 ;
var1Max = 2 ;

% Second Variable: Output Dir
var2Min = 0 ;
var2Max = 5 ;
 
%% Processing
var_1and2_Range = linspace(var1Min, var1Max, nTerms);


fileMatrix = cell(nTerms, varCount);
fileMatrix{1, 1} = 0.1 ;

for i = 2:nTerms % Excludes first term being 0
    
    var1Out = string(var_1and2_Range(i)) ;
    var2Out = append("/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/out/apr21_2/", string(var_1and2_Range(i)));
    
    fileMatrix{i, 1} = var1Out ;
    fileMatrix{i, 2} = var2Out ;

end

writecell(fileMatrix,'build_vars_in.txt','Delimiter',',');
type 'build_vars_in.txt'


