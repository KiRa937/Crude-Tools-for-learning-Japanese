set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
   start /wait mokuro --parent_dir %%x
)
