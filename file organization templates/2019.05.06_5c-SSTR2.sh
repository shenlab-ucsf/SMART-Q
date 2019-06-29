cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-39
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-39-1
SSTR2-5C-39-2
SSTR2-5C-39-3
SSTR2-5C-39-4
SSTR2-5C-39-5
SSTR2-5C-39-6
SSTR2-5C-39-7)
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

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-40
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-40-1
SSTR2-5C-40-2
SSTR2-5C-40-3
SSTR2-5C-40-4
SSTR2-5C-40-5
SSTR2-5C-40-6
SSTR2-5C-40-7
SSTR2-5C-40-8)
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

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-41
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-41-1
SSTR2-5C-41-2
SSTR2-5C-41-3
SSTR2-5C-41-4
SSTR2-5C-41-5
SSTR2-5C-41-6
SSTR2-5C-41-7
SSTR2-5C-41-8
SSTR2-5C-41-9)
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

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-42
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-42-1
SSTR2-5C-42-2
SSTR2-5C-42-3
SSTR2-5C-42-4
SSTR2-5C-42-5
SSTR2-5C-42-6
SSTR2-5C-42-7)
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

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-43
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-43-1
SSTR2-5C-43-2
SSTR2-5C-43-3
SSTR2-5C-43-4
SSTR2-5C-43-5
SSTR2-5C-43-6
SSTR2-5C-43-7
SSTR2-5C-43-8
SSTR2-5C-43-9)
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

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-44
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-44-1
SSTR2-5C-44-2
SSTR2-5C-44-3
SSTR2-5C-44-4)
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

cd /Users/sbergenholtz/Applications/starfish
nameBeforeDot=SSTR2-5C-45
new_dir=rnascope_5c_SSTR2
fileType=lif
gene_name=SSTR2
dirs=(SSTR2-5C-45-1
SSTR2-5C-45-2
SSTR2-5C-45-3
SSTR2-5C-45-4
SSTR2-5C-45-5
SSTR2-5C-45-6
SSTR2-5C-45-7
SSTR2-5C-45-8
SSTR2-5C-45-9
SSTR2-5C-45-10)
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
