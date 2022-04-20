%% Inputs
nTerms = 5; % Enter number of sims to run
varCount = 2; % Number of variables to write data for

% First Variable: Bending Modulus
var1Min = 0;
var1Max = 1;

% Second Variable: Output Dir
var2Min = 0;
var2Max = 1;
 
%% Processing
var_1and2_Range = linspace(var1Min, var1Max, nTerms);


fileMatrix = cell(nTerms, varCount);

for i = 1:nTerms
    
    var1Out = string(var_1and2_Range(i)) ;
    var2Out = append("/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/out/apr21/", string(var_1and2_Range(i)));
    
    fileMatrix{i, 1} = var1Out ;
    fileMatrix{i, 2} = var2Out ;

end

writecell(fileMatrix,'build_vars_in.txt','Delimiter',',')
type 'build_vars_in.txt'


