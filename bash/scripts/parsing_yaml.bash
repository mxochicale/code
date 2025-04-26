###############################################################################
# Usage: bash parsing_yaml.bash

#https://perfecto25.medium.com/handle-bash-config-file-variables-like-a-pro-957dc9a838ed
#https://gist.github.com/masukomi/e587aa6fd4f042496871 

function parse_yaml {
   local prefix=$2
   local s='[[:space:]]*' w='[a-zA-Z0-9_]*' fs=$(echo @|tr @ '\034')
   sed -ne "s|^\($s\):|\1|" \
        -e "s|^\($s\)\($w\)$s:$s[\"']\(.*\)[\"']$s\$|\1$fs\2$fs\3|p" \
        -e "s|^\($s\)\($w\)$s:$s\(.*\)$s\$|\1$fs\2$fs\3|p"  $1 |
   awk -F$fs '{
      indent = length($1)/2;
      vname[indent] = $2;
      for (i in vname) {if (i > indent) {delete vname[i]}}
      if (length($3) > 0) {
         vn=""; for (i=0; i<indent; i++) {vn=(vn)(vname[i])("_")}
         printf("%s%s%s=\"%s\"\n", "'$prefix'",vn, $2, $3);
      }
   }'
}


SCRIPT_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_PATH/../

eval $(parse_yaml config_files/config_sample.yaml)
echo $company_address # outputs “123 new city”
echo $company_phone_EU #outputs “2–1234–3433–33444”

eval $(parse_yaml config_files/config_sample1.yaml)
echo $global_verbose
echo $global_debugging_header
echo $output_file


