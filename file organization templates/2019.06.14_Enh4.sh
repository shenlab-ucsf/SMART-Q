cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot="Enh 4 3D"
new_dir=rnascope_enh4
fileType=lif
gene_name=mNPC
dirs=(Series010
Series009
Series008
Series007
Series006
Series005
Series004
Series002
Series001
Series028
Series027
Series026
Series025
Series024)
raw_image_dir=/Users/sbergenholtz/Downloads/mNPC-3d-1-selected/output
for ((i = 0; i < ${#dirs[@]}; i++)); do
    mkdir -p $new_dir/"${dirs[$i]}"/raw
    mkdir $new_dir/"${dirs[$i]}"/formatted
    mv "$raw_image_dir/${nameBeforeDot}.${fileType}"*" ${dirs[$i]} "*"C="*".tif" "$new_dir/${dirs[$i]}/raw"
    mv "$raw_image_dir/${nameBeforeDot}.${fileType}"*" ${dirs[$i]} "*"zplane"*"txt" "$new_dir/${dirs[$i]}/raw"
    mv "$new_dir/${dirs[$i]}/raw/"*"zplane_num.txt" "$new_dir/${dirs[$i]}/raw/zplane_num.txt"
done

cd $new_dir
for ((i = 0; i < ${#dirs[@]}; i++)); do
    echo ""
    echo "${dirs[$i]}"
    zplane_num=$(cat "${dirs[$i]}/raw/zplane_num.txt")
    python3 ../formatting/2019.06.14_formatRNAscopeData_mNPC.py "${dirs[$i]}/raw" "${dirs[$i]}/formatted" $new_dir "$nameBeforeDot" $fileType "${dirs[$i]}" $zplane_num
    echo "{\"version\": \"0.0.0\", \"mappings\": [{\"codeword\": [{\"c\": 0, \"r\": 0, \"v\": 1.0}], \"target\": \"$gene_name\"}]}" > "${dirs[$i]}/formatted/codebook.json"
done

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-40
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(Series023
Series021
Series019
Series018
Series017
Series016
Series015
Series014
Series011)
raw_image_dir=/Users/sbergenholtz/Downloads/5c-SSTR2/output
for ((i = 0; i < ${#dirs[@]}; i++)); do
    mkdir -p $new_dir/"${dirs[$i]}"/raw
    mkdir $new_dir/"${dirs[$i]}"/formatted
    mv "$raw_image_dir/${nameBeforeDot}.${fileType}"*" ${dirs[$i]} "*"C="*".tif" "$new_dir/${dirs[$i]}/raw"
    mv "$raw_image_dir/${nameBeforeDot}.${fileType}"*" ${dirs[$i]} "*"zplane"*"txt" "$new_dir/${dirs[$i]}/raw"
    mv "$new_dir/${dirs[$i]}/raw/"*"zplane_num.txt" "$new_dir/${dirs[$i]}/raw/zplane_num.txt"
done

cd $new_dir
for ((i = 0; i < ${#dirs[@]}; i++)); do
    echo ""
    echo "${dirs[$i]}"
    zplane_num=$(cat "${dirs[$i]}/raw/zplane_num.txt")
    python3 ../formatting/2019.05.03_formatRNAscopeData_test-TNC.py "${dirs[$i]}/raw" "${dirs[$i]}/formatted" $new_dir "$nameBeforeDot" $fileType "${dirs[$i]}" $zplane_num
    echo "{\"version\": \"0.0.0\", \"mappings\": [{\"codeword\": [{\"c\": 0, \"r\": 0, \"v\": 1.0}], \"target\": \"$gene_name\"}]}" > "${dirs[$i]}/formatted/codebook.json"
done

