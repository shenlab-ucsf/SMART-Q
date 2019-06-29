cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=test-TNC-27.26
new_dir=rnascope_test-TNC
fileType=lif
gene_name=TNC
dirs=(26-GW17
27-GW19)
raw_image_dir=/Users/sbergenholtz/Downloads/test-TNC/output
for ((i = 0; i < ${#dirs[@]}; i++)); do
    mkdir -p $new_dir/"${dirs[$i]}"/raw
    mkdir $new_dir/"${dirs[$i]}"/formatted
    cp "$raw_image_dir/${nameBeforeDot}.${fileType}"*" ${dirs[$i]} "*"C="*".tif" "$new_dir/${dirs[$i]}/raw"
    cp "$raw_image_dir/${nameBeforeDot}.${fileType}"*" ${dirs[$i]} "*"zplane"*"txt" "$new_dir/${dirs[$i]}/raw"
    mv "$new_dir/${dirs[$i]}/raw/"*"zplane_num.txt" "$new_dir/${dirs[$i]}/raw/zplane_num.txt"
done

cd $new_dir
for ((i = 0; i < ${#dirs[@]}; i++)); do
    zplane_num=$(cat "${dirs[$i]}/raw/zplane_num.txt")
    python3 ../formatting/2019.05.03_formatRNAscopeData_test-TNC.py "${dirs[$i]}/raw" "${dirs[$i]}/formatted" $new_dir "$nameBeforeDot" $fileType "${dirs[$i]}" $zplane_num
    echo "{\"version\": \"0.0.0\", \"mappings\": [{\"codeword\": [{\"c\": 0, \"r\": 0, \"v\": 1.0}], \"target\": \"$gene_name\"}]}" > "${dirs[$i]}/formatted/codebook.json"
done
