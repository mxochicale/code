# creation logs


## Sat  2 Dec 05:03:35 GMT 2023

```
=================================================================================
2023-12-02 04:53:31.157Z: Configuration starting...
2023-12-02 04:53:31.233Z: Cloning...
2023-12-02 04:53:31.272Z: $ git -C "/var/lib/docker/codespacemount/workspace" clone --branch "49-codespaces" --depth 1 https://github.com/mxochicale/code "/var/lib/docker/codespacemount/workspace/code"
2023-12-02 04:53:31.342Z: Cloning into '/var/lib/docker/codespacemount/workspace/code'...
2023-12-02 04:53:34.452Z: git process exited with exit code 0
2023-12-02 04:53:34.466Z: $ git -C "/var/lib/docker/codespacemount/workspace/code" config --local remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
2023-12-02 04:53:34.473Z: git process exited with exit code 0

=================================================================================
2023-12-02 04:53:35.069Z: Creating container...
2023-12-02 04:53:35.147Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/code --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --skip-post-create --config "/var/lib/docker/codespacemount/workspace/code/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2023-12-02 04:53:35.329Z: @devcontainers/cli 0.52.1. Node.js v18.17.1. linux 6.2.0-1016-azure x64.
2023-12-02 04:53:35.849Z: $ docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /tmp/devcontainercli-root/container-features/0.52.1-1701492815831/Dockerfile-with-features -t vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 --target dev_containers_target_stage --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /var/lib/docker/codespacemount/workspace/code
2023-12-02 04:53:36.313Z: #0 building with "default" instance using docker driver2023-12-02 04:53:36.322Z: 
2023-12-02 04:53:36.329Z: 
2023-12-02 04:53:36.335Z: #1 [internal] load .dockerignore2023-12-02 04:53:36.339Z: 
2023-12-02 04:53:36.342Z: #1 transferring context:2023-12-02 04:53:36.348Z: 
2023-12-02 04:53:36.454Z: #1 transferring context: 2B done
#1 DONE 0.2s

#2 [internal] load build definition from Dockerfile-with-features
2023-12-02 04:53:36.459Z: #2 transferring dockerfile: 2.50kB 0.0s done
#2 DONE 0.3s
2023-12-02 04:53:36.604Z: 
#3 [internal] load metadata for mcr.microsoft.com/devcontainers/miniconda:0-3
2023-12-02 04:53:36.889Z: #3 DONE 0.4s
2023-12-02 04:53:37.040Z: 
#4 [dev_container_auto_added_stage_label 1/3] FROM mcr.microsoft.com/devcontainers/miniconda:0-3@sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d
2023-12-02 04:53:37.048Z: #4 resolve mcr.microsoft.com/devcontainers/miniconda:0-3@sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d 0.1s done
2023-12-02 04:53:37.170Z: #4 ...2023-12-02 04:53:37.176Z: 

#5 [internal] load build context
#5 transferring context: 603B done
#5 DONE 0.2s

#4 [dev_container_auto_added_stage_label 1/3] FROM mcr.microsoft.com/devcontainers/miniconda:0-3@sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d
#4 sha256:533777e6c0c2310801735cdde71f4f441cf66b628c411ff97e20752b1d6cc86d 1.61kB / 1.61kB done
#4 sha256:c0d89f1c49a26e118bca52d16564d4ca0c851a7616eccfbd3f35a61e759786a6 24.54kB / 24.54kB done
#4 sha256:fbdfa74a59754288e14a6690f1d9a2498467cc83c939a7bcdb65d71f23596b5f 4.47kB / 4.47kB done
2023-12-02 04:53:37.318Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 13.73MB / 55.06MB 0.2s
2023-12-02 04:53:37.323Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 0B / 15.76MB 0.2s
#4 sha256:9a11a33b016bcaf1d0bd4a0857c13c9dc9486d5eb19d808d5c237d0cb271b99a 406B / 406B 0.2s done2023-12-02 04:53:37.331Z: 
2023-12-02 04:53:37.417Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 25.17MB / 55.06MB 0.3s
#4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 9.44MB / 15.76MB 0.3s
2023-12-02 04:53:37.422Z: #4 sha256:b837e19a13f10adaa26316a877e8a3b54df5cf7543914009d2ee02b41d64378f 0B / 134B 0.3s
2023-12-02 04:53:37.519Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 35.65MB / 55.06MB 0.4s2023-12-02 04:53:37.527Z: 
2023-12-02 04:53:37.547Z: #4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 15.76MB / 15.76MB 0.4s2023-12-02 04:53:37.566Z: 
2023-12-02 04:53:37.585Z: #4 sha256:b837e19a13f10adaa26316a877e8a3b54df5cf7543914009d2ee02b41d64378f 134B / 134B 0.4s done2023-12-02 04:53:37.603Z: 
2023-12-02 04:53:37.621Z: #4 sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d 0B / 223B 0.4s2023-12-02 04:53:37.630Z: 
2023-12-02 04:53:37.637Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 41.94MB / 55.06MB 0.6s2023-12-02 04:53:37.641Z: 
2023-12-02 04:53:37.774Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 55.06MB / 55.06MB 0.6s
#4 sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 15.76MB / 15.76MB 0.6s done
#4 sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d 223B / 223B 0.6s done
#4 sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c 0B / 232B 0.6s
2023-12-02 04:53:37.924Z: #4 sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c 232B / 232B 0.7s
#4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 0B / 108.29MB 0.7s
2023-12-02 04:53:38.074Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 16.78MB / 108.29MB 0.9s2023-12-02 04:53:38.078Z: 
2023-12-02 04:53:38.197Z: #4 sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 55.06MB / 55.06MB 1.0s done
2023-12-02 04:53:38.203Z: #4 sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c 232B / 232B 1.0s done2023-12-02 04:53:38.205Z: 
2023-12-02 04:53:38.209Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 27.26MB / 108.29MB 1.1s2023-12-02 04:53:38.211Z: 
2023-12-02 04:53:38.214Z: #4 extracting sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb2023-12-02 04:53:38.217Z: 
2023-12-02 04:53:38.299Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 35.65MB / 108.29MB 1.1s2023-12-02 04:53:38.304Z: 
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 0B / 155.98MB 1.1s
2023-12-02 04:53:38.418Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 52.43MB / 108.29MB 1.3s2023-12-02 04:53:38.438Z: 
2023-12-02 04:53:38.457Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 18.87MB / 155.98MB 1.3s2023-12-02 04:53:38.473Z: 
2023-12-02 04:53:38.486Z: #4 sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9 638B / 638B 1.1s done2023-12-02 04:53:38.499Z: 
2023-12-02 04:53:38.507Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 0B / 118.40MB 1.3s2023-12-02 04:53:38.513Z: 
2023-12-02 04:53:38.644Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 62.55MB / 108.29MB 1.6s2023-12-02 04:53:38.656Z: 
2023-12-02 04:53:38.671Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 33.55MB / 155.98MB 1.6s2023-12-02 04:53:38.679Z: 
2023-12-02 04:53:38.691Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 8.39MB / 118.40MB 1.6s2023-12-02 04:53:38.702Z: 
2023-12-02 04:53:38.753Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 68.16MB / 108.29MB 1.7s
2023-12-02 04:53:38.903Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 75.50MB / 108.29MB 1.8s2023-12-02 04:53:38.906Z: 
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 42.99MB / 155.98MB 1.8s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 16.78MB / 118.40MB 1.8s
2023-12-02 04:53:39.131Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 93.32MB / 108.29MB 2.1s2023-12-02 04:53:39.135Z: 
2023-12-02 04:53:39.143Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 58.43MB / 155.98MB 2.1s2023-12-02 04:53:39.158Z: 
2023-12-02 04:53:39.171Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 32.51MB / 118.40MB 2.1s2023-12-02 04:53:39.179Z: 
2023-12-02 04:53:39.239Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 38.80MB / 118.40MB 2.2s
2023-12-02 04:53:39.345Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 107.12MB / 108.29MB 2.3s
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 73.40MB / 155.98MB 2.3s
2023-12-02 04:53:39.448Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 49.28MB / 118.40MB 2.4s
2023-12-02 04:53:39.600Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 82.84MB / 155.98MB 2.5s2023-12-02 04:53:39.615Z: 
2023-12-02 04:53:39.747Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 55.86MB / 118.40MB 2.6s
2023-12-02 04:53:39.843Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 95.42MB / 155.98MB 2.8s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 65.01MB / 118.40MB 2.8s
2023-12-02 04:53:40.092Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 103.56MB / 155.98MB 2.9s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 75.50MB / 118.40MB 2.9s
2023-12-02 04:53:40.214Z: #4 sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 108.29MB / 108.29MB 2.9s done2023-12-02 04:53:40.226Z: 
#4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 113.25MB / 155.98MB 3.0s
#4 sha256:857523023f3af2b5bd1a8e05e269fa461162a454beb866f2e32551c7356fd0b8 0B / 122B 3.0s
2023-12-02 04:53:40.330Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 134.22MB / 155.98MB 3.2s
2023-12-02 04:53:40.337Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 82.84MB / 118.40MB 3.2s
#4 sha256:857523023f3af2b5bd1a8e05e269fa461162a454beb866f2e32551c7356fd0b8 122B / 122B 3.1s done
#4 sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22 0B / 605B 3.2s
2023-12-02 04:53:40.479Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 142.61MB / 155.98MB 3.3s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 92.27MB / 118.40MB 3.3s
#4 sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22 605B / 605B 3.3s done
2023-12-02 04:53:40.630Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 100.66MB / 118.40MB 3.5s
#4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 262.14kB / 35.86MB 3.5s
2023-12-02 04:53:40.794Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 155.98MB / 155.98MB 3.7s
#4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 108.00MB / 118.40MB 3.7s
#4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 10.49MB / 35.86MB 3.7s
2023-12-02 04:53:41.088Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 15.73MB / 35.86MB 4.0s2023-12-02 04:53:41.107Z: 
2023-12-02 04:53:41.191Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 117.44MB / 118.40MB 4.1s
#4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 19.27MB / 35.86MB 4.1s
2023-12-02 04:53:41.299Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 25.17MB / 35.86MB 4.1s
2023-12-02 04:53:41.415Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 30.41MB / 35.86MB 4.2s
2023-12-02 04:53:41.532Z: #4 sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 155.98MB / 155.98MB 4.4s done
#4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 35.86MB / 35.86MB 4.5s
#4 sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e 0B / 289B 4.5s
2023-12-02 04:53:41.679Z: #4 sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e 289B / 289B 4.5s
2023-12-02 04:53:42.371Z: #4 sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 118.40MB / 118.40MB 5.1s done
2023-12-02 04:53:42.517Z: #4 sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 35.86MB / 35.86MB 5.3s done2023-12-02 04:53:42.520Z: 
#4 sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e 289B / 289B 5.4s done
#4 sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346 412B / 412B 5.4s
#4 sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 0B / 32B 5.4s
2023-12-02 04:53:42.618Z: #4 sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B 5.5s done2023-12-02 04:53:42.621Z: 
2023-12-02 04:53:42.754Z: #4 sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346 412B / 412B 5.5s done
#4 sha256:1fbeb5db8b38e923a081350f3d836fb3b593c83f50566f296561558143d16f11 130B / 130B 5.6s done2023-12-02 04:53:42.756Z: 
#4 sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 225B / 225B 5.6s
#4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 0B / 60.61MB 5.6s
#4 sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c 0B / 240B 5.6s
2023-12-02 04:53:42.876Z: #4 sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 225B / 225B 5.7s done2023-12-02 04:53:42.878Z: 
#4 sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c 240B / 240B 5.7s done
#4 sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 0B / 1.99MB 5.7s
2023-12-02 04:53:42.986Z: #4 sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 1.99MB / 1.99MB 5.8s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 0B / 99.55MB 5.8s
2023-12-02 04:53:43.122Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 17.63MB / 60.61MB 6.0s2023-12-02 04:53:43.129Z: 
2023-12-02 04:53:43.137Z: #4 sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 1.99MB / 1.99MB 5.9s done2023-12-02 04:53:43.140Z: 
2023-12-02 04:53:43.142Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 12.58MB / 99.55MB 6.0s2023-12-02 04:53:43.160Z: 
2023-12-02 04:53:43.246Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 23.07MB / 60.61MB 6.2s
2023-12-02 04:53:43.394Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 26.21MB / 60.61MB 6.3s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 17.83MB / 99.55MB 6.3s
2023-12-02 04:53:43.567Z: #4 extracting sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 5.3s
#4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 30.41MB / 60.61MB 6.5s
2023-12-02 04:53:43.578Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 22.89MB / 99.55MB 6.5s
2023-12-02 04:53:43.883Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 38.99MB / 60.61MB 6.7s
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 32.51MB / 99.55MB 6.7s
2023-12-02 04:53:44.025Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 59.42MB / 60.61MB 7.0s2023-12-02 04:53:44.031Z: 
2023-12-02 04:53:44.035Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 51.38MB / 99.55MB 7.0s2023-12-02 04:53:44.042Z: 
2023-12-02 04:53:44.180Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 59.77MB / 99.55MB 7.0s
2023-12-02 04:53:44.317Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 70.69MB / 99.55MB 7.2s2023-12-02 04:53:44.322Z: 
2023-12-02 04:53:44.629Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 83.89MB / 99.55MB 7.4s2023-12-02 04:53:44.632Z: 
2023-12-02 04:53:44.717Z: #4 sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 60.61MB / 60.61MB 7.6s done
#4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 95.58MB / 99.55MB 7.6s2023-12-02 04:53:44.727Z: 
2023-12-02 04:53:45.094Z: #4 extracting sha256:ddf874abf16cc990e0fd75a154a34ca0a03ee310ad895a18fb62ae15bf4171fb 6.9s done
2023-12-02 04:53:45.217Z: #4 sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 99.55MB / 99.55MB 8.1s done
2023-12-02 04:53:45.368Z: #4 extracting sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e2023-12-02 04:53:45.371Z: 
2023-12-02 04:53:45.875Z: #4 extracting sha256:5c1459d3ab8b5e46ac1a0a00134fe2f7b693474eb6d75ace97ecbe811a6f5b0e 0.5s done
2023-12-02 04:53:46.476Z: #4 extracting sha256:9a11a33b016bcaf1d0bd4a0857c13c9dc9486d5eb19d808d5c237d0cb271b99a done
2023-12-02 04:53:46.620Z: #4 extracting sha256:b837e19a13f10adaa26316a877e8a3b54df5cf7543914009d2ee02b41d64378f done
#4 extracting sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d2023-12-02 04:53:46.623Z: 
2023-12-02 04:53:46.770Z: #4 extracting sha256:be88e9b1429e6abe1be4803e5f9560c271a407bd97941c12e81be9025abdab2d done
2023-12-02 04:53:46.922Z: #4 extracting sha256:469dc137be941824529e4f076cc2bbc129231c822962ad32580a4e2cd452253c done2023-12-02 04:53:46.924Z: 
2023-12-02 04:53:47.073Z: #4 extracting sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d2023-12-02 04:53:47.078Z: 
2023-12-02 04:53:51.978Z: #4 extracting sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 5.0s2023-12-02 04:53:52.012Z: 
2023-12-02 04:53:52.552Z: #4 extracting sha256:3b292f769942f54bc020381ae83ced4308d50f972ba512ad14b0489d4c4fc14d 5.5s done
2023-12-02 04:53:53.274Z: #4 extracting sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1
2023-12-02 04:53:57.753Z: #4 extracting sha256:7f92c98c9f975e511b894e4df6baf8396924428ddbc7920d0fe13404b70fbca1 4.4s done
2023-12-02 04:54:00.116Z: #4 extracting sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9
2023-12-02 04:54:00.266Z: #4 extracting sha256:f7abe09e5d5e4def17605244e9a4f2e8203b1d8d544fa30396d5ec42e6c47bf9 done2023-12-02 04:54:00.272Z: 
2023-12-02 04:54:00.416Z: #4 extracting sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681
2023-12-02 04:54:05.510Z: #4 extracting sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 5.0s
2023-12-02 04:54:06.254Z: #4 extracting sha256:5c10dec97b644a5f2a5514817462f2aba5205eb27aa8fb482e9978f2b187b681 5.8s done
2023-12-02 04:54:07.150Z: #4 extracting sha256:857523023f3af2b5bd1a8e05e269fa461162a454beb866f2e32551c7356fd0b8
2023-12-02 04:54:07.275Z: #4 extracting sha256:857523023f3af2b5bd1a8e05e269fa461162a454beb866f2e32551c7356fd0b8 done
#4 extracting sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22
2023-12-02 04:54:07.426Z: #4 extracting sha256:af0f8691d92b92416b19654d847770431abe5077d51bd1f815dcdf834804ff22 done2023-12-02 04:54:07.429Z: 
2023-12-02 04:54:07.576Z: #4 extracting sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c
2023-12-02 04:54:09.170Z: #4 extracting sha256:a5f5243ec26f765b90acd2506eb615faaed46a306c1f5a1804b434b72cc8435c 1.6s done
2023-12-02 04:54:09.889Z: #4 extracting sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e
2023-12-02 04:54:10.018Z: #4 extracting sha256:af7055f83fa381583c03a343562a0c407db2d45bd28d4e323034c8f06d2f2a2e done2023-12-02 04:54:10.026Z: 
#4 extracting sha256:1fbeb5db8b38e923a081350f3d836fb3b593c83f50566f296561558143d16f11
2023-12-02 04:54:10.168Z: #4 extracting sha256:1fbeb5db8b38e923a081350f3d836fb3b593c83f50566f296561558143d16f11 done2023-12-02 04:54:10.176Z: 
#4 extracting sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346
2023-12-02 04:54:10.317Z: #4 extracting sha256:f130883feb0eb350abe241dc9409fb73dd51704ad3ae92b536563eb149b33346 done
2023-12-02 04:54:10.458Z: #4 extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 done
#4 extracting sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8
2023-12-02 04:54:10.602Z: #4 extracting sha256:7ec8d5cae060f1455aec6189e1de7858b03dc8073c461a5e717fed7c336d28b8 done2023-12-02 04:54:10.607Z: 
#4 extracting sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c
2023-12-02 04:54:10.752Z: #4 extracting sha256:9da9948bb761fa37083d3c9a1fd71e7e3a93951fb0786bf3cab014068fbbe55c done
2023-12-02 04:54:10.903Z: #4 extracting sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566
2023-12-02 04:54:12.732Z: #4 extracting sha256:59d5b1cf8ef097657e4c2157443131e4e14997efb3a0042f4f7bd43bc4c8d566 1.8s done
2023-12-02 04:54:13.482Z: #4 extracting sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720
2023-12-02 04:54:13.626Z: #4 extracting sha256:cdb217fcffc2286bc4a98dd2a882800210e9563cac126d6be43c3c92aad2d720 0.2s done2023-12-02 04:54:13.629Z: 
2023-12-02 04:54:13.896Z: #4 extracting sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c502023-12-02 04:54:13.903Z: 
2023-12-02 04:54:18.630Z: #4 extracting sha256:39b3578ce9aac4f755f5c2ce9b7e9b3a79dca1791dde502c3241cc9de18c2c50 4.7s done
2023-12-02 04:54:22.539Z: #4 DONE 45.6s2023-12-02 04:54:22.543Z: 

#6 [dev_container_auto_added_stage_label 2/3] COPY .devcontainer/environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
2023-12-02 04:54:22.643Z: #6 DONE 0.2s

#7 [dev_container_auto_added_stage_label 3/3] RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env create -f /tmp/conda-tmp/environment.yml; fi     && rm -rf /tmp/conda-tmp
2023-12-02 04:54:24.002Z: #7 1.255 Collecting package metadata (repodata.json): ...working... 2023-12-02 04:55:43.252Z: done2023-12-02 04:55:43.259Z: 
2023-12-02 04:55:43.270Z: #7 80.56 Solving environment: ...working... 2023-12-02 04:55:45.801Z: done2023-12-02 04:55:45.805Z: 
#7 83.16 
#7 83.16 
#7 83.16 ==> WARNING: A newer version of conda exists. <==
#7 83.16   current version: 23.9.0
#7 83.16   latest version: 23.10.0
#7 83.16 
#7 83.16 Please update conda by running
#7 83.16 
2023-12-02 04:55:45.808Z: #7 83.16     $ conda update -n base -c defaults conda
#7 83.16 
#7 83.16 Or to minimize the number of packages updated during conda update use
#7 83.16 
#7 83.16      conda install conda=23.10.0
#7 83.16 
#7 83.16 
2023-12-02 04:55:49.070Z: #7 86.43 2023-12-02 04:55:49.074Z: 
#7 86.43 Downloading and Extracting Packages: ...working... done
#7 86.43 Preparing transaction: ...working... 2023-12-02 04:55:49.371Z: done2023-12-02 04:55:49.380Z: 
#7 86.61 Verifying transaction: ...working... 2023-12-02 04:55:50.425Z: done2023-12-02 04:55:50.438Z: 
#7 87.66 Executing transaction: ...working... 2023-12-02 04:55:53.134Z: done
2023-12-02 04:55:53.286Z: #7 90.55 Installing pip dependencies: ...working... 2023-12-02 04:56:12.092Z: Ran pip subprocess with arguments:2023-12-02 04:56:12.097Z: 
#7 109.3 ['/opt/conda/envs/demoVE/bin/python', '-m', 'pip', 'install', '-U', '-r', '/tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt', '--exists-action=b']
#7 109.3 Pip subprocess output:
#7 109.3 Collecting opencv-python-headless (from -r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 1))
#7 109.3   Downloading opencv_python_headless-4.8.1.78-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (19 kB)2023-12-02 04:56:12.104Z: 
#7 109.3 Collecting ipykernel (from -r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading ipykernel-6.27.1-py3-none-any.whl.metadata (6.3 kB)
#7 109.3 Collecting matplotlib (from -r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading matplotlib-3.8.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
#7 109.3 Collecting numpy>=1.21.2 (from opencv-python-headless->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 1))
#7 109.3   Downloading numpy-1.26.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (61 kB)
#7 109.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 kB 2.1 MB/s eta 0:00:00
#7 109.3 Collecting comm>=0.1.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
2023-12-02 04:56:12.112Z: #7 109.3   Downloading comm-0.2.0-py3-none-any.whl.metadata (3.7 kB)
#7 109.3 Collecting debugpy>=1.6.5 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading debugpy-1.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.0 kB)
#7 109.3 Collecting ipython>=7.23.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading ipython-8.18.1-py3-none-any.whl.metadata (6.0 kB)
#7 109.3 Collecting jupyter-client>=6.1.12 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading jupyter_client-8.6.0-py3-none-any.whl.metadata (8.3 kB)
#7 109.3 Collecting jupyter-core!=5.0.*,>=4.12 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading jupyter_core-5.5.0-py3-none-any.whl.metadata (3.4 kB)
#7 109.3 Collecting matplotlib-inline>=0.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading matplotlib_inline-0.1.6-py3-none-any.whl (9.4 kB)
#7 109.3 Collecting nest-asyncio (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))2023-12-02 04:56:12.121Z: 
#7 109.3   Downloading nest_asyncio-1.5.8-py3-none-any.whl.metadata (2.8 kB)
#7 109.3 Collecting packaging (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading packaging-23.2-py3-none-any.whl.metadata (3.2 kB)
#7 109.3 Collecting psutil (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading psutil-5.9.6-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (21 kB)
#7 109.3 Collecting pyzmq>=20 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading pyzmq-25.1.1-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (4.9 kB)
#7 109.3 Collecting tornado>=6.1 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
2023-12-02 04:56:12.127Z: #7 109.3   Downloading tornado-6.4-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.5 kB)
#7 109.3 Collecting traitlets>=5.4.0 (from ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading traitlets-5.14.0-py3-none-any.whl.metadata (10 kB)
#7 109.3 Collecting contourpy>=1.0.1 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading contourpy-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.8 kB)
#7 109.3 Collecting cycler>=0.10 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
#7 109.3 Collecting fonttools>=4.22.0 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading fonttools-4.45.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (155 kB)2023-12-02 04:56:12.132Z: 
#7 109.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 kB 5.0 MB/s eta 0:00:00
#7 109.3 Collecting kiwisolver>=1.3.1 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading kiwisolver-1.4.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.4 kB)
#7 109.3 Collecting pillow>=8 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (9.5 kB)
#7 109.3 Collecting pyparsing>=2.3.1 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)
#7 109.3 Collecting python-dateutil>=2.7 (from matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)2023-12-02 04:56:12.137Z: 
#7 109.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 1.5 MB/s eta 0:00:00
#7 109.3 Collecting decorator (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading decorator-5.1.1-py3-none-any.whl (9.1 kB)
#7 109.3 Collecting jedi>=0.16 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading jedi-0.19.1-py2.py3-none-any.whl.metadata (22 kB)
#7 109.3 Collecting prompt-toolkit<3.1.0,>=3.0.41 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading prompt_toolkit-3.0.41-py3-none-any.whl.metadata (6.5 kB)
#7 109.3 Collecting pygments>=2.4.0 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading pygments-2.17.2-py3-none-any.whl.metadata (2.6 kB)
2023-12-02 04:56:12.142Z: #7 109.3 Collecting stack-data (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
#7 109.3 Collecting pexpect>4.3 (from ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
#7 109.3 Collecting platformdirs>=2.5 (from jupyter-core!=5.0.*,>=4.12->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading platformdirs-4.0.0-py3-none-any.whl.metadata (11 kB)
#7 109.3 Collecting six>=1.5 (from python-dateutil>=2.7->matplotlib->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 3))
#7 109.3   Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
#7 109.3 Collecting parso<0.9.0,>=0.8.3 (from jedi>=0.16->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
2023-12-02 04:56:12.149Z: #7 109.3   Downloading parso-0.8.3-py2.py3-none-any.whl (100 kB)
#7 109.3      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.8/100.8 kB 3.7 MB/s eta 0:00:00
#7 109.3 Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
#7 109.3 Collecting wcwidth (from prompt-toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading wcwidth-0.2.12-py2.py3-none-any.whl.metadata (14 kB)
#7 109.3 Collecting executing>=1.2.0 (from stack-data->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading executing-2.0.1-py2.py3-none-any.whl.metadata (9.0 kB)
#7 109.3 Collecting asttokens>=2.1.0 (from stack-data->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
2023-12-02 04:56:12.153Z: #7 109.3   Downloading asttokens-2.4.1-py2.py3-none-any.whl.metadata (5.2 kB)
#7 109.3 Collecting pure-eval (from stack-data->ipython>=7.23.1->ipykernel->-r /tmp/conda-tmp/condaenv.tj1h9r0m.requirements.txt (line 2))
#7 109.3   Downloading pure_eval-0.2.2-py3-none-any.whl (11 kB)
#7 109.3 Downloading opencv_python_headless-4.8.1.78-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (49.1 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.1/49.1 MB 24.7 MB/s eta 0:00:00
#7 109.3 Downloading ipykernel-6.27.1-py3-none-any.whl (114 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.6/114.6 kB 4.2 MB/s eta 0:00:00
#7 109.3 Downloading matplotlib-3.8.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.6 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 59.6 MB/s eta 0:00:002023-12-02 04:56:12.160Z: 
#7 109.3 Downloading comm-0.2.0-py3-none-any.whl (7.0 kB)
#7 109.3 Downloading contourpy-1.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (313 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 313.4/313.4 kB 10.5 MB/s eta 0:00:00
#7 109.3 Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
#7 109.3 Downloading debugpy-1.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 46.4 MB/s eta 0:00:00
#7 109.3 Downloading fonttools-4.45.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.9 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 56.6 MB/s eta 0:00:00
#7 109.3 Downloading ipython-8.18.1-py3-none-any.whl (808 kB)2023-12-02 04:56:12.166Z: 
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 808.2/808.2 kB 16.7 MB/s eta 0:00:00
#7 109.3 Downloading jupyter_client-8.6.0-py3-none-any.whl (105 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 105.9/105.9 kB 4.0 MB/s eta 0:00:00
#7 109.3 Downloading jupyter_core-5.5.0-py3-none-any.whl (28 kB)
#7 109.3 Downloading kiwisolver-1.4.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.4 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 32.4 MB/s eta 0:00:00
#7 109.3 Downloading numpy-1.26.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (18.2 MB)2023-12-02 04:56:12.171Z: 
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 51.0 MB/s eta 0:00:00
#7 109.3 Downloading packaging-23.2-py3-none-any.whl (53 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 53.0/53.0 kB 1.2 MB/s eta 0:00:00
#7 109.3 Downloading Pillow-10.1.0-cp311-cp311-manylinux_2_28_x86_64.whl (3.6 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 47.7 MB/s eta 0:00:00
#7 109.3 Downloading pyparsing-3.1.1-py3-none-any.whl (103 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.1/103.1 kB 3.6 MB/s eta 0:00:00
#7 109.3 Downloading pyzmq-25.1.1-cp311-cp311-manylinux_2_28_x86_64.whl (1.1 MB)
2023-12-02 04:56:12.177Z: #7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 27.3 MB/s eta 0:00:00
#7 109.3 Downloading tornado-6.4-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (435 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 435.4/435.4 kB 14.3 MB/s eta 0:00:00
#7 109.3 Downloading traitlets-5.14.0-py3-none-any.whl (85 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 85.2/85.2 kB 2.8 MB/s eta 0:00:00
#7 109.3 Downloading nest_asyncio-1.5.8-py3-none-any.whl (5.3 kB)
#7 109.3 Downloading psutil-5.9.6-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (283 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 283.6/283.6 kB 9.3 MB/s eta 0:00:00
#7 109.3 Downloading jedi-0.19.1-py2.py3-none-any.whl (1.6 MB)
2023-12-02 04:56:12.181Z: #7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 32.1 MB/s eta 0:00:00
#7 109.3 Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.8/63.8 kB 2.4 MB/s eta 0:00:00
#7 109.3 Downloading platformdirs-4.0.0-py3-none-any.whl (17 kB)
#7 109.3 Downloading prompt_toolkit-3.0.41-py3-none-any.whl (385 kB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 385.5/385.5 kB 13.3 MB/s eta 0:00:00
#7 109.3 Downloading pygments-2.17.2-py3-none-any.whl (1.2 MB)
#7 109.3    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 27.0 MB/s eta 0:00:00
#7 109.3 Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
2023-12-02 04:56:12.186Z: #7 109.3 Downloading asttokens-2.4.1-py2.py3-none-any.whl (27 kB)
#7 109.3 Downloading executing-2.0.1-py2.py3-none-any.whl (24 kB)
#7 109.3 Downloading wcwidth-0.2.12-py2.py3-none-any.whl (34 kB)
#7 109.3 Installing collected packages: wcwidth, pure-eval, ptyprocess, traitlets, tornado, six, pyzmq, pyparsing, pygments, psutil, prompt-toolkit, platformdirs, pillow, pexpect, parso, packaging, numpy, nest-asyncio, kiwisolver, fonttools, executing, decorator, debugpy, cycler, python-dateutil, opencv-python-headless, matplotlib-inline, jupyter-core, jedi, contourpy, comm, asttokens, stack-data, matplotlib, jupyter-client, ipython, ipykernel
#7 109.3 Successfully installed asttokens-2.4.1 comm-0.2.0 contourpy-1.2.0 cycler-0.12.1 debugpy-1.8.0 decorator-5.1.1 executing-2.0.1 fonttools-4.45.1 ipykernel-6.27.1 ipython-8.18.1 jedi-0.19.1 jupyter-client-8.6.0 jupyter-core-5.5.0 kiwisolver-1.4.5 matplotlib-3.8.2 matplotlib-inline-0.1.6 nest-asyncio-1.5.8 numpy-1.26.2 opencv-python-headless-4.8.1.78 packaging-23.2 parso-0.8.3 pexpect-4.9.0 pillow-10.1.0 platformdirs-4.0.0 prompt-toolkit-3.0.41 psutil-5.9.6 ptyprocess-0.7.0 pure-eval-0.2.2 pygments-2.17.2 pyparsing-3.1.1 python-dateutil-2.8.2 pyzmq-25.1.1 six-1.16.0 stack-data-0.6.3 tornado-6.4 traitlets-5.14.0 wcwidth-0.2.12
#7 109.3 
#7 109.3 done
#7 109.3 #
#7 109.3 # To activate this environment, use
#7 109.3 #
2023-12-02 04:56:12.191Z: #7 109.3 #     $ conda activate demoVE
#7 109.3 #
#7 109.3 # To deactivate an active environment, use
#7 109.3 #
#7 109.3 #     $ conda deactivate
#7 109.3 
2023-12-02 04:56:19.625Z: #7 DONE 116.9s
2023-12-02 04:56:19.629Z: 
#8 preparing layers for inline cache
2023-12-02 04:56:30.862Z: #8 DONE 11.3s

#9 exporting to image
#9 exporting layers done
#9 writing image sha256:e5c8f2251c43c6e6206c09e60b0bdc4827af28fd2e9e89d83dbaa9138e1072d8 0.0s done
#9 naming to docker.io/library/vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606
2023-12-02 04:56:30.912Z: #9 naming to docker.io/library/vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 0.0s done
#9 DONE 0.1s2023-12-02 04:56:30.917Z: 
2023-12-02 04:56:30.926Z: Stop: Run: docker buildx build --load --build-arg BUILDKIT_INLINE_CACHE=1 -f /tmp/devcontainercli-root/container-features/0.52.1-1701492815831/Dockerfile-with-features -t vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 --target dev_containers_target_stage --build-arg _DEV_CONTAINERS_BASE_IMAGE=dev_container_auto_added_stage_label /var/lib/docker/codespacemount/workspace/code
2023-12-02 04:56:30.954Z: $127.0.0.1 --cap-add sys_nice --network host --entrypoint /bin/sh vsc-code-ebc7ff1bb830c9ab527f890f7f31279e8e4979e92a94006398168157f6921606 -c echo Container started
2023-12-02 04:56:31.280Z: Container started
2023-12-02 04:56:31.649Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/code
2023-12-02 04:56:31.659Z: devcontainer process exited with exit code 0

=================================================================================
2023-12-02 04:56:32.936Z: Running blocking commands...
2023-12-02 04:56:32.977Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/code --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --user-data-folder /var/lib/docker/codespacemount/.persistedshare --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --omit-config-remote-env-from-metadata --skip-non-blocking-commands --expect-existing-container --config "/var/lib/docker/codespacemount/workspace/code/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2023-12-02 04:56:33.224Z: @devcontainers/cli 0.52.1. Node.js v18.17.1. linux 6.2.0-1016-azure x64.
2023-12-02 04:56:33.547Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/code
2023-12-02 04:56:33.580Z: devcontainer process exited with exit code 0

=================================================================================
2023-12-02 04:56:33.669Z: Configuring codespace...
2023-12-02 04:56:33.792Z: $ cp -r /root/.docker /var/lib/docker/codespacemount/.persistedshare
2023-12-02 04:56:33.803Z: cp process exited with exit code 0
2023-12-02 04:56:33.806Z: $ rm -rf /home/vscode/.docker
2023-12-02 04:56:33.919Z: rm process exited with exit code 0
2023-12-02 04:56:33.924Z: $ ln -sfn /workspaces/.codespaces/.persistedshare/.docker /home/vscode/.docker
2023-12-02 04:56:34.015Z: ln process exited with exit code 0
2023-12-02 04:56:34.018Z: $ chown -R vscode /workspaces/.codespaces/.persistedshare/.docker
2023-12-02 04:56:34.112Z: chown process exited with exit code 0

=================================================================================
2023-12-02 04:56:34.155Z: Running commands...
2023-12-02 04:56:34.159Z: $ devcontainer up --id-label Type=codespaces --workspace-folder /var/lib/docker/codespacemount/workspace/code --expect-existing-container --skip-post-attach --mount type=bind,source=/.codespaces/agent/mount/cache,target=/vscode --container-data-folder .vscode-remote/data/Machine --container-system-data-folder /var/vscode-remote --log-level trace --log-format json --update-remote-user-uid-default never --mount-workspace-git-root false --config "/var/lib/docker/codespacemount/workspace/code/.devcontainer/devcontainer.json" --override-config /root/.codespaces/shared/merged_devcontainer.json --default-user-env-probe loginInteractiveShell --container-session-data-folder /workspaces/.codespaces/.persistedshare/devcontainers-cli/cache --secrets-file /root/.codespaces/shared/user-secrets-envs.json
2023-12-02 04:56:34.337Z: @devcontainers/cli 0.52.1. Node.js v18.17.1. linux 6.2.0-1016-azure x64.
2023-12-02 04:56:34.646Z: Running the postCreateCommand from devcontainer.json...

2023-12-02 04:56:34.662Z: conda init
2023-12-02 04:56:35.836Z: no change     /opt/conda/condabin/conda
no change     /opt/conda/bin/conda
no change     /opt/conda/bin/conda-env
no change     /opt/conda/bin/activate
no change     /opt/conda/bin/deactivate
no change     /opt/conda/etc/profile.d/conda.sh
no change     /opt/conda/etc/fish/conf.d/conda.fish
no change     /opt/conda/shell/condabin/Conda.psm1
no change     /opt/conda/shell/condabin/conda-hook.ps1
no change     /opt/conda/lib/python3.11/site-packages/xontrib/conda.xsh
no change     /opt/conda/etc/profile.d/conda.csh
modified      /home/vscode/.bashrc=> For changes to take effect, close and re-open your current shell. <==

2023-12-02 04:56:35.918Z: Outcome: success User: vscode WorkspaceFolder: /workspaces/code
2023-12-02 04:56:36.048Z: devcontainer process exited with exit code 0

=================================================================================
2023-12-02 04:56:36.061Z: Finished configuring codespace.
```
